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


import ApiClient from './ApiClient';
import AcceptChangeRequest200Response from './model/AcceptChangeRequest200Response';
import AcceptChangeRequestRequest from './model/AcceptChangeRequestRequest';
import AddSecret200Response from './model/AddSecret200Response';
import AddUser200Response from './model/AddUser200Response';
import AddUser200ResponseData from './model/AddUser200ResponseData';
import AddUser200ResponseDataAddedUser from './model/AddUser200ResponseDataAddedUser';
import AgentKey from './model/AgentKey';
import AllCampaigns200Response from './model/AllCampaigns200Response';
import AllCampaigns200ResponseData from './model/AllCampaigns200ResponseData';
import ApiEndpointsInner from './model/ApiEndpointsInner';
import ApiGeneralInformations200Response from './model/ApiGeneralInformations200Response';
import ApiGeneralInformations200ResponseData from './model/ApiGeneralInformations200ResponseData';
import ApiInformations200Response from './model/ApiInformations200Response';
import ApiInformations200ResponseData from './model/ApiInformations200ResponseData';
import ApiInformations200ResponseDataEndpointsInner from './model/ApiInformations200ResponseDataEndpointsInner';
import ApiSubInformations200Response from './model/ApiSubInformations200Response';
import ApiVersion from './model/ApiVersion';
import ApiVersionAllInner from './model/ApiVersionAllInner';
import ApiVersions from './model/ApiVersions';
import ApplyPolicyAllNodes200Response from './model/ApplyPolicyAllNodes200Response';
import ApplyPolicyAllNodes200ResponseDataInner from './model/ApplyPolicyAllNodes200ResponseDataInner';
import BrandingConf from './model/BrandingConf';
import CampaignDetails from './model/CampaignDetails';
import CampaignDetailsDetails from './model/CampaignDetailsDetails';
import CampaignDetailsInfo from './model/CampaignDetailsInfo';
import CampaignDetailsInfoSchedule from './model/CampaignDetailsInfoSchedule';
import CampaignDetailsInfoStatus from './model/CampaignDetailsInfoStatus';
import CampaignEventDetails from './model/CampaignEventDetails';
import CampaignEventDetailsStatus from './model/CampaignEventDetailsStatus';
import CampaignEventNodeResult from './model/CampaignEventNodeResult';
import CampaignEventNodeResultNodesInner from './model/CampaignEventNodeResultNodesInner';
import CampaignEventNodeResultNodesInnerResult from './model/CampaignEventNodeResultNodesInnerResult';
import CampaignEventNodeResultNodesInnerResultSoftwareUpdatedInner from './model/CampaignEventNodeResultNodesInnerResultSoftwareUpdatedInner';
import CampaignEventResult from './model/CampaignEventResult';
import CampaignEventResultNodesInner from './model/CampaignEventResultNodesInner';
import CampaignScheduleMonthly from './model/CampaignScheduleMonthly';
import CampaignScheduleMonthlyEnd from './model/CampaignScheduleMonthlyEnd';
import CampaignScheduleMonthlyStart from './model/CampaignScheduleMonthlyStart';
import CampaignScheduleOneshot from './model/CampaignScheduleOneshot';
import CampaignScheduleWeekly from './model/CampaignScheduleWeekly';
import CampaignScheduleWeeklyEnd from './model/CampaignScheduleWeeklyEnd';
import CampaignScheduleWeeklyStart from './model/CampaignScheduleWeeklyStart';
import CampaignSoftwareUpdate from './model/CampaignSoftwareUpdate';
import CampaignSoftwareUpdateSoftwareUpdateInner from './model/CampaignSoftwareUpdateSoftwareUpdateInner';
import CampaignStatusArchived from './model/CampaignStatusArchived';
import CampaignStatusDisabled from './model/CampaignStatusDisabled';
import CampaignStatusEnabled from './model/CampaignStatusEnabled';
import CampaignSystemUpdate from './model/CampaignSystemUpdate';
import CategoriesTree from './model/CategoriesTree';
import ChangePendingNodeStatus200Response from './model/ChangePendingNodeStatus200Response';
import ChangePendingNodeStatus200ResponseData from './model/ChangePendingNodeStatus200ResponseData';
import ChangePendingNodeStatusRequest from './model/ChangePendingNodeStatusRequest';
import ChangeRequest from './model/ChangeRequest';
import ChangeRequestChanges from './model/ChangeRequestChanges';
import ChangeRequestChangesRulesInner from './model/ChangeRequestChangesRulesInner';
import ChangeRequestDetails200Response from './model/ChangeRequestDetails200Response';
import Check from './model/Check';
import CheckCVE200Response from './model/CheckCVE200Response';
import CheckCVE200ResponseData from './model/CheckCVE200ResponseData';
import CheckDirective200Response from './model/CheckDirective200Response';
import Color from './model/Color';
import ComplianceDirectiveId from './model/ComplianceDirectiveId';
import ComplianceDirectiveIdData from './model/ComplianceDirectiveIdData';
import CreateArchive200Response from './model/CreateArchive200Response';
import CreateArchive200ResponseData from './model/CreateArchive200ResponseData';
import CreateDataSource200Response from './model/CreateDataSource200Response';
import CreateDataSource200ResponseData from './model/CreateDataSource200ResponseData';
import CreateDirective200Response from './model/CreateDirective200Response';
import CreateGroup200Response from './model/CreateGroup200Response';
import CreateGroupCategory200Response from './model/CreateGroupCategory200Response';
import CreateGroupCategory200ResponseData from './model/CreateGroupCategory200ResponseData';
import CreateNodes200Response from './model/CreateNodes200Response';
import CreateNodes200ResponseData from './model/CreateNodes200ResponseData';
import CreateParameter200Response from './model/CreateParameter200Response';
import CreateRule200Response from './model/CreateRule200Response';
import CreateRuleCategory200Response from './model/CreateRuleCategory200Response';
import CreateRuleCategory200ResponseData from './model/CreateRuleCategory200ResponseData';
import CreateTechnique200Response from './model/CreateTechnique200Response';
import CreateTechnique200ResponseData from './model/CreateTechnique200ResponseData';
import CreateTechnique200ResponseDataTechniques from './model/CreateTechnique200ResponseDataTechniques';
import CveCheck from './model/CveCheck';
import CveCheckPackagesInner from './model/CveCheckPackagesInner';
import CveCheckScore from './model/CveCheckScore';
import CveDetails from './model/CveDetails';
import CveDetailsCvssv2 from './model/CveDetailsCvssv2';
import CveDetailsCvssv3 from './model/CveDetailsCvssv3';
import Datasource from './model/Datasource';
import DatasourceRunParameters from './model/DatasourceRunParameters';
import DatasourceRunParametersSchedule from './model/DatasourceRunParametersSchedule';
import DatasourceType from './model/DatasourceType';
import DatasourceTypeParameters from './model/DatasourceTypeParameters';
import DatasourceTypeParametersHeadersInner from './model/DatasourceTypeParametersHeadersInner';
import DatasourceTypeParametersRequestMode from './model/DatasourceTypeParametersRequestMode';
import DeclineChangeRequest200Response from './model/DeclineChangeRequest200Response';
import DeleteCampaign200Response from './model/DeleteCampaign200Response';
import DeleteCampaignEvent200Response from './model/DeleteCampaignEvent200Response';
import DeleteDataSource200Response from './model/DeleteDataSource200Response';
import DeleteDirective200Response from './model/DeleteDirective200Response';
import DeleteGroup200Response from './model/DeleteGroup200Response';
import DeleteGroupCategory200Response from './model/DeleteGroupCategory200Response';
import DeleteNode200Response from './model/DeleteNode200Response';
import DeleteParameter200Response from './model/DeleteParameter200Response';
import DeleteParameter500Response from './model/DeleteParameter500Response';
import DeleteRule200Response from './model/DeleteRule200Response';
import DeleteRuleCategory200Response from './model/DeleteRuleCategory200Response';
import DeleteRuleCategory200ResponseData from './model/DeleteRuleCategory200ResponseData';
import DeleteSecret200Response from './model/DeleteSecret200Response';
import DeleteTechnique200Response from './model/DeleteTechnique200Response';
import DeleteTechnique200ResponseData from './model/DeleteTechnique200ResponseData';
import DeleteTechnique200ResponseDataTechniques from './model/DeleteTechnique200ResponseDataTechniques';
import DeleteUser200Response from './model/DeleteUser200Response';
import DeleteUser200ResponseData from './model/DeleteUser200ResponseData';
import DeleteUser200ResponseDataDeletedUser from './model/DeleteUser200ResponseDataDeletedUser';
import DemoteToNode200Response from './model/DemoteToNode200Response';
import Directive from './model/Directive';
import DirectiveDetails200Response from './model/DirectiveDetails200Response';
import DirectiveNew from './model/DirectiveNew';
import DirectiveNodeCompliance from './model/DirectiveNodeCompliance';
import DirectiveNodeComplianceComplianceDetails from './model/DirectiveNodeComplianceComplianceDetails';
import DirectiveRuleCompliance from './model/DirectiveRuleCompliance';
import DirectiveRuleComplianceComponentsInner from './model/DirectiveRuleComplianceComponentsInner';
import DirectiveTagsInner from './model/DirectiveTagsInner';
import EditorTechnique from './model/EditorTechnique';
import EditorTechniqueCallsInner from './model/EditorTechniqueCallsInner';
import FileWatcherRestart200Response from './model/FileWatcherRestart200Response';
import FileWatcherStart200Response from './model/FileWatcherStart200Response';
import FileWatcherStop200Response from './model/FileWatcherStop200Response';
import GetAllCampaignEvents200Response from './model/GetAllCampaignEvents200Response';
import GetAllCampaignEvents200ResponseData from './model/GetAllCampaignEvents200ResponseData';
import GetAllCve200Response from './model/GetAllCve200Response';
import GetAllCve200ResponseData from './model/GetAllCve200ResponseData';
import GetAllDataSources200Response from './model/GetAllDataSources200Response';
import GetAllDataSources200ResponseData from './model/GetAllDataSources200ResponseData';
import GetAllSecrets200Response from './model/GetAllSecrets200Response';
import GetAllSecrets200ResponseData from './model/GetAllSecrets200ResponseData';
import GetAllSecrets200ResponseDataSecretsInner from './model/GetAllSecrets200ResponseDataSecretsInner';
import GetAllSettings200Response from './model/GetAllSettings200Response';
import GetAllSettings200ResponseData from './model/GetAllSettings200ResponseData';
import GetAllSettings200ResponseDataSettings from './model/GetAllSettings200ResponseDataSettings';
import GetAllSettings200ResponseDataSettingsAllowedNetworksInner from './model/GetAllSettings200ResponseDataSettingsAllowedNetworksInner';
import GetAllowedNetworks200Response from './model/GetAllowedNetworks200Response';
import GetAllowedNetworks200ResponseData from './model/GetAllowedNetworks200ResponseData';
import GetAllowedNetworks200ResponseDataSettings from './model/GetAllowedNetworks200ResponseDataSettings';
import GetBrandingConf200Response from './model/GetBrandingConf200Response';
import GetBrandingConf200ResponseData from './model/GetBrandingConf200ResponseData';
import GetCVECheckConfiguration200Response from './model/GetCVECheckConfiguration200Response';
import GetCVECheckConfiguration200ResponseData from './model/GetCVECheckConfiguration200ResponseData';
import GetCVEList200Response from './model/GetCVEList200Response';
import GetCVEListRequest from './model/GetCVEListRequest';
import GetCampaign200Response from './model/GetCampaign200Response';
import GetCampaignEventResult200Response from './model/GetCampaignEventResult200Response';
import GetCampaignEventResult200ResponseData from './model/GetCampaignEventResult200ResponseData';
import GetCampaignEventResultForNode200Response from './model/GetCampaignEventResultForNode200Response';
import GetCampaignEventResultForNode200ResponseData from './model/GetCampaignEventResultForNode200ResponseData';
import GetCampaignHistory200Response from './model/GetCampaignHistory200Response';
import GetCampaignHistory200ResponseData from './model/GetCampaignHistory200ResponseData';
import GetCve200Response from './model/GetCve200Response';
import GetDataSource200Response from './model/GetDataSource200Response';
import GetDirectiveComplianceId200Response from './model/GetDirectiveComplianceId200Response';
import GetDirectivesCompliance200Response from './model/GetDirectivesCompliance200Response';
import GetDirectivesCompliance200ResponseData from './model/GetDirectivesCompliance200ResponseData';
import GetDirectivesCompliance200ResponseDataDirectivesCompliance from './model/GetDirectivesCompliance200ResponseDataDirectivesCompliance';
import GetDirectivesCompliance200ResponseDataDirectivesComplianceComplianceDetails from './model/GetDirectivesCompliance200ResponseDataDirectivesComplianceComplianceDetails';
import GetEventsCampaign200Response from './model/GetEventsCampaign200Response';
import GetGlobalCompliance200Response from './model/GetGlobalCompliance200Response';
import GetGlobalCompliance200ResponseData from './model/GetGlobalCompliance200ResponseData';
import GetGlobalCompliance200ResponseDataGlobalCompliance from './model/GetGlobalCompliance200ResponseDataGlobalCompliance';
import GetGlobalCompliance200ResponseDataGlobalComplianceComplianceDetails from './model/GetGlobalCompliance200ResponseDataGlobalComplianceComplianceDetails';
import GetGroupCategoryDetails200Response from './model/GetGroupCategoryDetails200Response';
import GetGroupTree200Response from './model/GetGroupTree200Response';
import GetGroupTree200ResponseData from './model/GetGroupTree200ResponseData';
import GetHealthcheckResult200Response from './model/GetHealthcheckResult200Response';
import GetLastCVECheck200Response from './model/GetLastCVECheck200Response';
import GetLastCVECheck200ResponseData from './model/GetLastCVECheck200ResponseData';
import GetNodeCompliance200Response from './model/GetNodeCompliance200Response';
import GetNodesCompliance200Response from './model/GetNodesCompliance200Response';
import GetNodesCompliance200ResponseData from './model/GetNodesCompliance200ResponseData';
import GetNodesCompliance200ResponseDataNodesInner from './model/GetNodesCompliance200ResponseDataNodesInner';
import GetNodesStatus200Response from './model/GetNodesStatus200Response';
import GetNodesStatus200ResponseData from './model/GetNodesStatus200ResponseData';
import GetNodesStatus200ResponseDataNodesInner from './model/GetNodesStatus200ResponseDataNodesInner';
import GetRole200Response from './model/GetRole200Response';
import GetRole200ResponseDataInner from './model/GetRole200ResponseDataInner';
import GetRuleCategoryDetails200Response from './model/GetRuleCategoryDetails200Response';
import GetRuleCategoryDetails200ResponseData from './model/GetRuleCategoryDetails200ResponseData';
import GetRuleCompliance200Response from './model/GetRuleCompliance200Response';
import GetRuleTree200Response from './model/GetRuleTree200Response';
import GetRuleTree200ResponseData from './model/GetRuleTree200ResponseData';
import GetRulesCompliance200Response from './model/GetRulesCompliance200Response';
import GetRulesCompliance200ResponseData from './model/GetRulesCompliance200ResponseData';
import GetRulesCompliance200ResponseDataRulesInner from './model/GetRulesCompliance200ResponseDataRulesInner';
import GetSecret200Response from './model/GetSecret200Response';
import GetSetting200Response from './model/GetSetting200Response';
import GetSetting200ResponseData from './model/GetSetting200ResponseData';
import GetStatus200Response from './model/GetStatus200Response';
import GetStatus200ResponseData from './model/GetStatus200ResponseData';
import GetSystemInfo200Response from './model/GetSystemInfo200Response';
import GetSystemInfo200ResponseData from './model/GetSystemInfo200ResponseData';
import GetSystemInfo200ResponseDataRudder from './model/GetSystemInfo200ResponseDataRudder';
import GetTechniqueAllVersion200Response from './model/GetTechniqueAllVersion200Response';
import GetTechniqueAllVersion200ResponseData from './model/GetTechniqueAllVersion200ResponseData';
import GetTechniqueAllVersion200ResponseDataTechniquesInner from './model/GetTechniqueAllVersion200ResponseDataTechniquesInner';
import GetTechniquesResources200Response from './model/GetTechniquesResources200Response';
import GetTechniquesResources200ResponseData from './model/GetTechniquesResources200ResponseData';
import GetUserInfo200Response from './model/GetUserInfo200Response';
import GetUserInfo200ResponseData from './model/GetUserInfo200ResponseData';
import Group from './model/Group';
import GroupCategory from './model/GroupCategory';
import GroupCategoryUpdate from './model/GroupCategoryUpdate';
import GroupDetails200Response from './model/GroupDetails200Response';
import GroupNew from './model/GroupNew';
import GroupNewQuery from './model/GroupNewQuery';
import GroupPropertiesInner from './model/GroupPropertiesInner';
import GroupQuery from './model/GroupQuery';
import GroupQueryWhereInner from './model/GroupQueryWhereInner';
import GroupUpdate from './model/GroupUpdate';
import Import200Response from './model/Import200Response';
import Import200ResponseData from './model/Import200ResponseData';
import ListAcceptedNodes200Response from './model/ListAcceptedNodes200Response';
import ListAcceptedNodes200ResponseData from './model/ListAcceptedNodes200ResponseData';
import ListArchives200Response from './model/ListArchives200Response';
import ListArchives200ResponseData from './model/ListArchives200ResponseData';
import ListArchives200ResponseDataFullInner from './model/ListArchives200ResponseDataFullInner';
import ListChangeRequests200Response from './model/ListChangeRequests200Response';
import ListChangeRequests200ResponseData from './model/ListChangeRequests200ResponseData';
import ListDirectives200Response from './model/ListDirectives200Response';
import ListDirectives200ResponseData from './model/ListDirectives200ResponseData';
import ListGroups200Response from './model/ListGroups200Response';
import ListGroups200ResponseData from './model/ListGroups200ResponseData';
import ListParameters200Response from './model/ListParameters200Response';
import ListParameters200ResponseData from './model/ListParameters200ResponseData';
import ListPendingNodes200Response from './model/ListPendingNodes200Response';
import ListRules200Response from './model/ListRules200Response';
import ListRules200ResponseData from './model/ListRules200ResponseData';
import ListTechniqueVersionDirectives200Response from './model/ListTechniqueVersionDirectives200Response';
import ListTechniques200Response from './model/ListTechniques200Response';
import ListTechniques200ResponseData from './model/ListTechniques200ResponseData';
import ListTechniquesDirectives200Response from './model/ListTechniquesDirectives200Response';
import ListTechniquesVersions200Response from './model/ListTechniquesVersions200Response';
import ListTechniquesVersions200ResponseData from './model/ListTechniquesVersions200ResponseData';
import ListUsers200Response from './model/ListUsers200Response';
import Logo from './model/Logo';
import MethodParameter from './model/MethodParameter';
import MethodParameterConstraints from './model/MethodParameterConstraints';
import Methods from './model/Methods';
import Methods200Response from './model/Methods200Response';
import Methods200ResponseData from './model/Methods200ResponseData';
import MethodsCondition from './model/MethodsCondition';
import MethodsDeprecated from './model/MethodsDeprecated';
import ModifyAllowedNetworks200Response from './model/ModifyAllowedNetworks200Response';
import ModifyAllowedNetworks200ResponseData from './model/ModifyAllowedNetworks200ResponseData';
import ModifyAllowedNetworksRequest from './model/ModifyAllowedNetworksRequest';
import ModifyAllowedNetworksRequestAllowedNetworks from './model/ModifyAllowedNetworksRequestAllowedNetworks';
import ModifySetting200Response from './model/ModifySetting200Response';
import ModifySettingRequest from './model/ModifySettingRequest';
import NodeAddInner from './model/NodeAddInner';
import NodeAddInnerPropertiesInner from './model/NodeAddInnerPropertiesInner';
import NodeComplianceComponent from './model/NodeComplianceComponent';
import NodeComplianceComponentValuesInner from './model/NodeComplianceComponentValuesInner';
import NodeComplianceComponentValuesInnerReportsInner from './model/NodeComplianceComponentValuesInnerReportsInner';
import NodeDetails200Response from './model/NodeDetails200Response';
import NodeFull from './model/NodeFull';
import NodeFullBios from './model/NodeFullBios';
import NodeFullControllersInner from './model/NodeFullControllersInner';
import NodeFullEnvironmentVariablesInner from './model/NodeFullEnvironmentVariablesInner';
import NodeFullFileSystemsInner from './model/NodeFullFileSystemsInner';
import NodeFullMachine from './model/NodeFullMachine';
import NodeFullManagementTechnologyDetails from './model/NodeFullManagementTechnologyDetails';
import NodeFullManagementTechnologyInner from './model/NodeFullManagementTechnologyInner';
import NodeFullMemoriesInner from './model/NodeFullMemoriesInner';
import NodeFullNetworkInterfacesInner from './model/NodeFullNetworkInterfacesInner';
import NodeFullOs from './model/NodeFullOs';
import NodeFullPortsInner from './model/NodeFullPortsInner';
import NodeFullProcessesInner from './model/NodeFullProcessesInner';
import NodeFullProcessorsInner from './model/NodeFullProcessorsInner';
import NodeFullSlotsInner from './model/NodeFullSlotsInner';
import NodeFullSoftwareInner from './model/NodeFullSoftwareInner';
import NodeFullSoftwareInnerLicense from './model/NodeFullSoftwareInnerLicense';
import NodeFullSoftwareUpdateInner from './model/NodeFullSoftwareUpdateInner';
import NodeFullSoundInner from './model/NodeFullSoundInner';
import NodeFullStorageInner from './model/NodeFullStorageInner';
import NodeFullTimezone from './model/NodeFullTimezone';
import NodeFullVideosInner from './model/NodeFullVideosInner';
import NodeFullVirtualMachinesInner from './model/NodeFullVirtualMachinesInner';
import NodeInheritedProperties from './model/NodeInheritedProperties';
import NodeInheritedProperties200Response from './model/NodeInheritedProperties200Response';
import NodeInheritedPropertiesPropertiesInner from './model/NodeInheritedPropertiesPropertiesInner';
import NodeInheritedPropertiesPropertiesInnerHierarchyInner from './model/NodeInheritedPropertiesPropertiesInnerHierarchyInner';
import NodeSettings from './model/NodeSettings';
import Os from './model/Os';
import Parameter from './model/Parameter';
import ParameterDetails200Response from './model/ParameterDetails200Response';
import PromoteToRelay200Response from './model/PromoteToRelay200Response';
import PurgeSoftware200Response from './model/PurgeSoftware200Response';
import QueueInformation200Response from './model/QueueInformation200Response';
import QueueInformation200ResponseData from './model/QueueInformation200ResponseData';
import ReadCVEfromFS200Response from './model/ReadCVEfromFS200Response';
import RegeneratePolicies200Response from './model/RegeneratePolicies200Response';
import RegeneratePolicies200ResponseData from './model/RegeneratePolicies200ResponseData';
import ReloadAll200Response from './model/ReloadAll200Response';
import ReloadAll200ResponseData from './model/ReloadAll200ResponseData';
import ReloadAllDatasourcesAllNodes200Response from './model/ReloadAllDatasourcesAllNodes200Response';
import ReloadAllDatasourcesOneNode200Response from './model/ReloadAllDatasourcesOneNode200Response';
import ReloadGroup200Response from './model/ReloadGroup200Response';
import ReloadGroups200Response from './model/ReloadGroups200Response';
import ReloadGroups200ResponseData from './model/ReloadGroups200ResponseData';
import ReloadOneDatasourceAllNodes200Response from './model/ReloadOneDatasourceAllNodes200Response';
import ReloadOneDatasourceOneNode200Response from './model/ReloadOneDatasourceOneNode200Response';
import ReloadTechniques200Response from './model/ReloadTechniques200Response';
import ReloadTechniques200ResponseData from './model/ReloadTechniques200ResponseData';
import ReloadUserConf200Response from './model/ReloadUserConf200Response';
import ReloadUserConf200ResponseData from './model/ReloadUserConf200ResponseData';
import ReloadUserConf200ResponseDataReload from './model/ReloadUserConf200ResponseDataReload';
import RemoveValidatedUser200Response from './model/RemoveValidatedUser200Response';
import RestoreArchive200Response from './model/RestoreArchive200Response';
import RestoreArchive200ResponseData from './model/RestoreArchive200ResponseData';
import Rule from './model/Rule';
import RuleCategory from './model/RuleCategory';
import RuleCategoryUpdate from './model/RuleCategoryUpdate';
import RuleComplianceComponent from './model/RuleComplianceComponent';
import RuleComplianceComponentComplianceDetails from './model/RuleComplianceComponentComplianceDetails';
import RuleComplianceComponentComponentsInner from './model/RuleComplianceComponentComponentsInner';
import RuleComplianceComponentComponentsInnerValuesInner from './model/RuleComplianceComponentComponentsInnerValuesInner';
import RuleComplianceComponentComponentsInnerValuesInnerReportsInner from './model/RuleComplianceComponentComponentsInnerValuesInnerReportsInner';
import RuleDetails200Response from './model/RuleDetails200Response';
import RuleNew from './model/RuleNew';
import RuleTarget from './model/RuleTarget';
import RuleTargetsInner from './model/RuleTargetsInner';
import RuleTargetsInnerExclude from './model/RuleTargetsInnerExclude';
import RuleTargetsInnerInclude from './model/RuleTargetsInnerInclude';
import RuleWithCategory from './model/RuleWithCategory';
import SaveCampaign200Response from './model/SaveCampaign200Response';
import SaveCampaignEvent200Response from './model/SaveCampaignEvent200Response';
import SaveWorkflowUser200Response from './model/SaveWorkflowUser200Response';
import SaveWorkflowUserRequest from './model/SaveWorkflowUserRequest';
import ScheduleCampaign200Response from './model/ScheduleCampaign200Response';
import Secrets from './model/Secrets';
import SetAllowedNetworks200Response from './model/SetAllowedNetworks200Response';
import SetAllowedNetworks200ResponseData from './model/SetAllowedNetworks200ResponseData';
import SetAllowedNetworksRequest from './model/SetAllowedNetworksRequest';
import TechniqueBlock from './model/TechniqueBlock';
import TechniqueBlockReportingLogic from './model/TechniqueBlockReportingLogic';
import TechniqueCategories200Response from './model/TechniqueCategories200Response';
import TechniqueCategories200ResponseData from './model/TechniqueCategories200ResponseData';
import TechniqueCategory from './model/TechniqueCategory';
import TechniqueMethodCall from './model/TechniqueMethodCall';
import TechniqueMethodCallParametersInner from './model/TechniqueMethodCallParametersInner';
import TechniqueParameter from './model/TechniqueParameter';
import TechniqueResource from './model/TechniqueResource';
import TechniqueRevisions200Response from './model/TechniqueRevisions200Response';
import TechniqueRevisions200ResponseData from './model/TechniqueRevisions200ResponseData';
import TechniquesResourcesInner from './model/TechniquesResourcesInner';
import TechniquesRevisionsInner from './model/TechniquesRevisionsInner';
import TechniquesVersionsInner from './model/TechniquesVersionsInner';
import Timezone from './model/Timezone';
import UpdateBRandingConf200Response from './model/UpdateBRandingConf200Response';
import UpdateCVE200Response from './model/UpdateCVE200Response';
import UpdateCVE200ResponseData from './model/UpdateCVE200ResponseData';
import UpdateCVECheckConfiguration200Response from './model/UpdateCVECheckConfiguration200Response';
import UpdateCVECheckConfigurationRequest from './model/UpdateCVECheckConfigurationRequest';
import UpdateCVERequest from './model/UpdateCVERequest';
import UpdateChangeRequest200Response from './model/UpdateChangeRequest200Response';
import UpdateChangeRequestRequest from './model/UpdateChangeRequestRequest';
import UpdateDataSource200Response from './model/UpdateDataSource200Response';
import UpdateDirective200Response from './model/UpdateDirective200Response';
import UpdateGroup200Response from './model/UpdateGroup200Response';
import UpdateGroupCategory200Response from './model/UpdateGroupCategory200Response';
import UpdateNode200Response from './model/UpdateNode200Response';
import UpdateParameter200Response from './model/UpdateParameter200Response';
import UpdatePolicies200Response from './model/UpdatePolicies200Response';
import UpdateRule200Response from './model/UpdateRule200Response';
import UpdateRule200ResponseData from './model/UpdateRule200ResponseData';
import UpdateRuleCategory200Response from './model/UpdateRuleCategory200Response';
import UpdateSecret200Response from './model/UpdateSecret200Response';
import UpdateUser200Response from './model/UpdateUser200Response';
import UpdateUser200ResponseData from './model/UpdateUser200ResponseData';
import UpdateUser200ResponseDataUpdatedUser from './model/UpdateUser200ResponseDataUpdatedUser';
import UploadInventory200Response from './model/UploadInventory200Response';
import Users from './model/Users';
import ValidatedUser from './model/ValidatedUser';
import APIInfoApi from './api/APIInfoApi';
import ArchivesApi from './api/ArchivesApi';
import BrandingApi from './api/BrandingApi';
import CVEApi from './api/CVEApi';
import CampaignsApi from './api/CampaignsApi';
import ChangeRequestsApi from './api/ChangeRequestsApi';
import ComplianceApi from './api/ComplianceApi';
import DataSourcesApi from './api/DataSourcesApi';
import DirectivesApi from './api/DirectivesApi';
import GroupsApi from './api/GroupsApi';
import InventoriesApi from './api/InventoriesApi';
import NodesApi from './api/NodesApi';
import ParametersApi from './api/ParametersApi';
import RulesApi from './api/RulesApi';
import ScaleOutRelayApi from './api/ScaleOutRelayApi';
import SecretManagementApi from './api/SecretManagementApi';
import SettingsApi from './api/SettingsApi';
import StatusApi from './api/StatusApi';
import SystemApi from './api/SystemApi';
import SystemUpdateCampaignsApi from './api/SystemUpdateCampaignsApi';
import TechniquesApi from './api/TechniquesApi';
import UserManagementApi from './api/UserManagementApi';


/**
* Download OpenAPI specification: [openapi.yml](openapi.yml)  # Introduction  Rudder exposes a REST API, enabling the user to interact with Rudder without using the webapp, for example in scripts or cronjobs.  ## Versioning  Each time the API is extended with new features (new functions, new parameters, new responses, ...), it will be assigned a new version number. This will allow you to keep your existing scripts (based on previous behavior). Versions will always be integers (no 2.1 or 3.3, just 2, 3, 4, ...) or &#x60;latest&#x60;.  You can change the version of the API used by setting it either within the url or in a header:  * the URL: each URL is prefixed by its version id, like &#x60;/api/version/function&#x60;.  &#x60;&#x60;&#x60;bash # Version 10 curl -X GET -H \&quot;X-API-Token: yourToken\&quot; https://rudder.example.com/rudder/api/10/rules # Latest curl -X GET -H \&quot;X-API-Token: yourToken\&quot; https://rudder.example.com/rudder/api/latest/rules # Wrong (not an integer) &#x3D;&gt; 404 not found curl -X GET -H \&quot;X-API-Token: yourToken\&quot; https://rudder.example.com/rudder/api/3.14/rules &#x60;&#x60;&#x60;  * the HTTP headers. You can add the **X-API-Version** header to your request. The value needs to be an integer or &#x60;latest&#x60;.  &#x60;&#x60;&#x60;bash # Version 10 curl -X GET -H \&quot;X-API-Token: yourToken\&quot; -H \&quot;X-API-Version: 10\&quot; https://rudder.example.com/rudder/api/rules # Wrong &#x3D;&gt; Error response indicating which versions are available curl -X GET -H \&quot;X-API-Token: yourToken\&quot; -H \&quot;X-API-Version: 3.14\&quot; https://rudder.example.com/rudder/api/rules &#x60;&#x60;&#x60;  In the future, we may declare some versions as deprecated, in order to remove them in a later version of Rudder, but we will never remove any versions without warning, or without a safe period of time to allow migration from previous versions.   &lt;h4&gt;Existing versions&lt;/h4&gt; &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th style&#x3D;\&quot;width: 20%\&quot;&gt;Version&lt;/th&gt;       &lt;th style&#x3D;\&quot;width: 20%\&quot;&gt;Rudder versions it appeared in&lt;/th&gt;       &lt;th style&#x3D;\&quot;width: 70%\&quot;&gt;Description&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;1&lt;/td&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;Never released (for internal use only)&lt;/td&gt;       &lt;td&gt;Experimental version&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;2 to 10 (deprecated)&lt;/td&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;4.3 and before&lt;/td&gt;       &lt;td&gt;These versions provided the core set of API features for rules, directives, nodes global parameters, change requests and compliance, rudder settings and system API&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;11&lt;/td&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;5.0&lt;/td&gt;       &lt;td&gt;New system API (replacing old localhost v1 api): status, maintenance operations and server behavior&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;12&lt;/td&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;6.0 and 6.1&lt;/td&gt;       &lt;td&gt;Node key management&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;13&lt;/td&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;6.2&lt;/td&gt;       &lt;td&gt;&lt;ul&gt;         &lt;li&gt;Node status endpoint&lt;/li&gt;         &lt;li&gt;System health check&lt;/li&gt;         &lt;li&gt;System maintenance job to purge software [that endpoint was back-ported in 6.1]&lt;/li&gt;       &lt;/ul&gt;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;14&lt;/td&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;7.0&lt;/td&gt;       &lt;td&gt;&lt;ul&gt;         &lt;li&gt;Secret management&lt;/li&gt;         &lt;li&gt;Directive tree&lt;/li&gt;         &lt;li&gt;Improve techniques management&lt;/li&gt;         &lt;li&gt;Demote a relay&lt;/li&gt;       &lt;/ul&gt;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;15&lt;/td&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;7.1&lt;/td&gt;       &lt;td&gt;&lt;ul&gt;         &lt;li&gt;Package updates in nodes&lt;/li&gt;       &lt;/ul&gt;&lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;16&lt;/td&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;7.2&lt;/td&gt;       &lt;td&gt;&lt;ul&gt;         &lt;li&gt;Create node API included from plugin&lt;/li&gt;         &lt;li&gt;Configuration archive import/export&lt;/li&gt;       &lt;/ul&gt;&lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt;   ## Response format  All responses from the API are in the JSON format.  &#x60;&#x60;&#x60;json {   \&quot;action\&quot;: \&quot;The name of the called function\&quot;,   \&quot;id\&quot;: \&quot;The ID of the element you want, if relevant\&quot;,   \&quot;result\&quot;: \&quot;The result of your action: success or error\&quot;,   \&quot;data\&quot;: \&quot;Only present if this is a success and depends on the function, it&#39;s usually a JSON object\&quot;,   \&quot;errorDetails\&quot;: \&quot;Only present if this is an error, it contains the error message\&quot; } &#x60;&#x60;&#x60;   * __Success__ responses are sent with the 200 HTTP (Success) code  * __Error__ responses are sent with a HTTP error code (mostly 5xx...)   ## HTTP method  Rudder&#39;s REST API is based on the usage of [HTTP methods](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html). We use them to indicate what action will be done by the request. Currently, we use four of them:   * **GET**: search or retrieve information (get rule details, get a group, ...)  * **PUT**: add new objects (create a directive, clone a Rule, ...)  * **DELETE**: remove objects (delete a node, delete a parameter, ...)  * **POST**: update existing objects (update a directive, reload a group, ...)   ## Parameters  ### General parameters  Some parameters are available for almost all API functions. They will be described in this section. They must be part of the query and can&#39;t be submitted in a JSON form.  #### Available for all requests  &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th style&#x3D;\&quot;width: 30%\&quot;&gt;Field&lt;/th&gt;       &lt;th style&#x3D;\&quot;width: 10%\&quot;&gt;Type&lt;/th&gt;       &lt;th style&#x3D;\&quot;width: 70%\&quot;&gt;Description&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;prettify&lt;/td&gt;       &lt;td&gt;&lt;b&gt;boolean&lt;/b&gt;&lt;br&gt;&lt;i&gt;optional&lt;/i&gt;&lt;/td&gt;       &lt;td&gt;         Determine if the answer should be prettified (human friendly) or not. We recommend using this for debugging purposes, but not for general script usage as this does add some unnecessary load on the server side.         &lt;p class&#x3D;\&quot;default-value\&quot;&gt;Default value: &lt;code&gt;false&lt;/code&gt;&lt;/p&gt;       &lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt;   #### Available for modification requests (PUT/POST/DELETE)  &lt;table&gt;   &lt;thead&gt;     &lt;tr&gt;       &lt;th style&#x3D;\&quot;width: 25%\&quot;&gt;Field&lt;/th&gt;       &lt;th style&#x3D;\&quot;width: 12%\&quot;&gt;Type&lt;/th&gt;       &lt;th style&#x3D;\&quot;width: 70%\&quot;&gt;Description&lt;/th&gt;     &lt;/tr&gt;   &lt;/thead&gt;   &lt;tbody&gt;     &lt;tr&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;reason&lt;/td&gt;       &lt;td&gt;&lt;b&gt;string&lt;/b&gt;&lt;br&gt;&lt;i&gt;optional&lt;/i&gt; or &lt;i&gt;required&lt;/i&gt;&lt;/td&gt;       &lt;td&gt;         Set a message to explain the change. If you set the reason messages to be mandatory in the web interface, failing to supply this value will lead to an error.         &lt;p class&#x3D;\&quot;default-value\&quot;&gt;Default value: &lt;code&gt;\&quot;\&quot;&lt;/code&gt;&lt;/p&gt;       &lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;changeRequestName&lt;/td&gt;       &lt;td&gt;&lt;b&gt;string&lt;/b&gt;&lt;br&gt;&lt;i&gt;optional&lt;/i&gt;&lt;/td&gt;       &lt;td&gt;         Set the change request name, is used only if workflows are enabled. The default value depends on the function called         &lt;p class&#x3D;\&quot;default-value\&quot;&gt;Default value: &lt;code&gt;A default string for each function&lt;/code&gt;&lt;/p&gt;       &lt;/td&gt;     &lt;/tr&gt;     &lt;tr&gt;       &lt;td class&#x3D;\&quot;code\&quot;&gt;changeRequestDescription&lt;/td&gt;       &lt;td&gt;&lt;b&gt;string&lt;/b&gt;&lt;br&gt;&lt;i&gt;optional&lt;/i&gt;&lt;/td&gt;       &lt;td&gt;         Set the change request description, is used only if workflows are enabled.         &lt;p class&#x3D;\&quot;default-value\&quot;&gt;Default value: &lt;code&gt;\&quot;\&quot;&lt;/code&gt;&lt;/p&gt;       &lt;/td&gt;     &lt;/tr&gt;   &lt;/tbody&gt; &lt;/table&gt;   ### Passing parameters  Parameters to the API can be sent:  * As part of the URL for resource identification  * As data for POST/PUT requests    * Directly in JSON format    * As request arguments  #### As part of the URL for resource identification  Parameters in URLs are used to indicate which resource you want to interact with. The function will not work if this resource is missing.  &#x60;&#x60;&#x60;bash # Get the Rule of ID \&quot;id\&quot; curl -H \&quot;X-API-Token: yourToken\&quot; https://rudder.example.com/rudder/api/latest/rules/id &#x60;&#x60;&#x60;    CAUTION: To avoid surprising behavior, do not put a &#39;/&#39; at the end of an URL: it would be interpreted as &#39;/[empty string parameter]&#39; and redirected to &#39;/index&#39;, likely not what you wanted to do.   #### Sending data for POST/PUT requests  ##### Directly in JSON format  JSON format is the preferred way to interact with Rudder API for creating or updating resources. You&#39;ll also have to set the *Content-Type* header to **application/json** (without it the JSON content would be ignored). In a &#x60;curl&#x60; &#x60;POST&#x60; request, that header can be provided with the &#x60;-H&#x60; parameter:  &#x60;&#x60;&#x60;bash curl -X POST -H \&quot;Content-Type: application/json\&quot; ... &#x60;&#x60;&#x60;  The supplied file must contain a valid JSON: strings need quotes, booleans and integers don&#39;t, etc.  The (human readable) format is:  &#x60;&#x60;&#x60;json {   \&quot;key1\&quot;: \&quot;value1\&quot;,   \&quot;key2\&quot;: false,   \&quot;key3\&quot;: 42 } &#x60;&#x60;&#x60;   Here is an example with inlined data:  &#x60;&#x60;&#x60;bash # Update the Rule &#39;id&#39; with a new name, disabled, and setting it one directive curl -X POST -H \&quot;X-API-Token: yourToken\&quot; -H  \&quot;Content-Type: application/json\&quot; https://rudder.example.com/rudder/api/rules/latest/{id}   -d &#39;{ \&quot;displayName\&quot;: \&quot;new name\&quot;, \&quot;enabled\&quot;: false, \&quot;directives\&quot;: \&quot;directiveId\&quot;}&#39; &#x60;&#x60;&#x60;  You can also pass a supply the JSON in a file:  &#x60;&#x60;&#x60;bash # Update the Rule &#39;id&#39; with a new name, disabled, and setting it one directive curl -X POST -H \&quot;X-API-Token: yourToken\&quot; -H \&quot;Content-Type: application/json\&quot; https://rudder.example.com/rudder/api/rules/latest/{id} -d @jsonParam &#x60;&#x60;&#x60;  Note that the general parameters view in the previous chapter cannot be passed in a JSON, and you will need to pass them a URL parameters if you want them to be taken into account (you can&#39;t mix JSON and request parameters):  &#x60;&#x60;&#x60;bash # Update the Rule &#39;id&#39; with a new name, disabled, and setting it one directive with reason message \&quot;Reason used\&quot; curl -X POST -H \&quot;X-API-Token: yourToken\&quot; -H \&quot;Content-Type: application/json\&quot; \&quot;https://rudder.example.com/rudder/api/rules/latest/{id}?reason&#x3D;Reason used\&quot; -d @jsonParam -d \&quot;reason&#x3D;Reason ignored\&quot; &#x60;&#x60;&#x60;  ##### Request parameters  In some cases, when you have little, simple data to update, JSON can feel bloated. In such cases, you can use request parameters. You will need to pass one parameter for each data you want to change.  Parameters follow the following schema:  &#x60;&#x60;&#x60; key&#x3D;value &#x60;&#x60;&#x60;  You can pass parameters by two means:  * As query parameters: At the end of your url, put a **?** then your first parameter and then a **&amp;** before next parameters. In that case, parameters need to be https://en.wikipedia.org/wiki/Percent-encoding[URL encoded]  &#x60;&#x60;&#x60;bash # Update the Rule &#39;id&#39; with a new name, disabled, and setting it one directive curl -X POST -H \&quot;X-API-Token: yourToken\&quot;  https://rudder.example.com/rudder/api/rules/latest/{id}?\&quot;displayName&#x3D;my new name\&quot;&amp;\&quot;enabled&#x3D;false\&quot;&amp;\&quot;directives&#x3D;aDirectiveId\&quot; &#x60;&#x60;&#x60;  * As request data: You can pass those parameters in the request data, they won&#39;t figure in the URL, making it lighter to read, You can pass a file that contains data.  &#x60;&#x60;&#x60;bash # Update the Rule &#39;id&#39; with a new name, disabled, and setting it one directive (in file directive-info.json) curl -X POST -H \&quot;X-API-Token: yourToken\&quot; https://rudder.example.com/rudder/api/rules/latest/{id} -d \&quot;displayName&#x3D;my new name\&quot; -d \&quot;enabled&#x3D;false\&quot; -d @directive-info.json &#x60;&#x60;&#x60; .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var RudderApi = require('index'); // See note below*.
* var xxxSvc = new RudderApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new RudderApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new RudderApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new RudderApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 17
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AcceptChangeRequest200Response model constructor.
     * @property {module:model/AcceptChangeRequest200Response}
     */
    AcceptChangeRequest200Response,

    /**
     * The AcceptChangeRequestRequest model constructor.
     * @property {module:model/AcceptChangeRequestRequest}
     */
    AcceptChangeRequestRequest,

    /**
     * The AddSecret200Response model constructor.
     * @property {module:model/AddSecret200Response}
     */
    AddSecret200Response,

    /**
     * The AddUser200Response model constructor.
     * @property {module:model/AddUser200Response}
     */
    AddUser200Response,

    /**
     * The AddUser200ResponseData model constructor.
     * @property {module:model/AddUser200ResponseData}
     */
    AddUser200ResponseData,

    /**
     * The AddUser200ResponseDataAddedUser model constructor.
     * @property {module:model/AddUser200ResponseDataAddedUser}
     */
    AddUser200ResponseDataAddedUser,

    /**
     * The AgentKey model constructor.
     * @property {module:model/AgentKey}
     */
    AgentKey,

    /**
     * The AllCampaigns200Response model constructor.
     * @property {module:model/AllCampaigns200Response}
     */
    AllCampaigns200Response,

    /**
     * The AllCampaigns200ResponseData model constructor.
     * @property {module:model/AllCampaigns200ResponseData}
     */
    AllCampaigns200ResponseData,

    /**
     * The ApiEndpointsInner model constructor.
     * @property {module:model/ApiEndpointsInner}
     */
    ApiEndpointsInner,

    /**
     * The ApiGeneralInformations200Response model constructor.
     * @property {module:model/ApiGeneralInformations200Response}
     */
    ApiGeneralInformations200Response,

    /**
     * The ApiGeneralInformations200ResponseData model constructor.
     * @property {module:model/ApiGeneralInformations200ResponseData}
     */
    ApiGeneralInformations200ResponseData,

    /**
     * The ApiInformations200Response model constructor.
     * @property {module:model/ApiInformations200Response}
     */
    ApiInformations200Response,

    /**
     * The ApiInformations200ResponseData model constructor.
     * @property {module:model/ApiInformations200ResponseData}
     */
    ApiInformations200ResponseData,

    /**
     * The ApiInformations200ResponseDataEndpointsInner model constructor.
     * @property {module:model/ApiInformations200ResponseDataEndpointsInner}
     */
    ApiInformations200ResponseDataEndpointsInner,

    /**
     * The ApiSubInformations200Response model constructor.
     * @property {module:model/ApiSubInformations200Response}
     */
    ApiSubInformations200Response,

    /**
     * The ApiVersion model constructor.
     * @property {module:model/ApiVersion}
     */
    ApiVersion,

    /**
     * The ApiVersionAllInner model constructor.
     * @property {module:model/ApiVersionAllInner}
     */
    ApiVersionAllInner,

    /**
     * The ApiVersions model constructor.
     * @property {module:model/ApiVersions}
     */
    ApiVersions,

    /**
     * The ApplyPolicyAllNodes200Response model constructor.
     * @property {module:model/ApplyPolicyAllNodes200Response}
     */
    ApplyPolicyAllNodes200Response,

    /**
     * The ApplyPolicyAllNodes200ResponseDataInner model constructor.
     * @property {module:model/ApplyPolicyAllNodes200ResponseDataInner}
     */
    ApplyPolicyAllNodes200ResponseDataInner,

    /**
     * The BrandingConf model constructor.
     * @property {module:model/BrandingConf}
     */
    BrandingConf,

    /**
     * The CampaignDetails model constructor.
     * @property {module:model/CampaignDetails}
     */
    CampaignDetails,

    /**
     * The CampaignDetailsDetails model constructor.
     * @property {module:model/CampaignDetailsDetails}
     */
    CampaignDetailsDetails,

    /**
     * The CampaignDetailsInfo model constructor.
     * @property {module:model/CampaignDetailsInfo}
     */
    CampaignDetailsInfo,

    /**
     * The CampaignDetailsInfoSchedule model constructor.
     * @property {module:model/CampaignDetailsInfoSchedule}
     */
    CampaignDetailsInfoSchedule,

    /**
     * The CampaignDetailsInfoStatus model constructor.
     * @property {module:model/CampaignDetailsInfoStatus}
     */
    CampaignDetailsInfoStatus,

    /**
     * The CampaignEventDetails model constructor.
     * @property {module:model/CampaignEventDetails}
     */
    CampaignEventDetails,

    /**
     * The CampaignEventDetailsStatus model constructor.
     * @property {module:model/CampaignEventDetailsStatus}
     */
    CampaignEventDetailsStatus,

    /**
     * The CampaignEventNodeResult model constructor.
     * @property {module:model/CampaignEventNodeResult}
     */
    CampaignEventNodeResult,

    /**
     * The CampaignEventNodeResultNodesInner model constructor.
     * @property {module:model/CampaignEventNodeResultNodesInner}
     */
    CampaignEventNodeResultNodesInner,

    /**
     * The CampaignEventNodeResultNodesInnerResult model constructor.
     * @property {module:model/CampaignEventNodeResultNodesInnerResult}
     */
    CampaignEventNodeResultNodesInnerResult,

    /**
     * The CampaignEventNodeResultNodesInnerResultSoftwareUpdatedInner model constructor.
     * @property {module:model/CampaignEventNodeResultNodesInnerResultSoftwareUpdatedInner}
     */
    CampaignEventNodeResultNodesInnerResultSoftwareUpdatedInner,

    /**
     * The CampaignEventResult model constructor.
     * @property {module:model/CampaignEventResult}
     */
    CampaignEventResult,

    /**
     * The CampaignEventResultNodesInner model constructor.
     * @property {module:model/CampaignEventResultNodesInner}
     */
    CampaignEventResultNodesInner,

    /**
     * The CampaignScheduleMonthly model constructor.
     * @property {module:model/CampaignScheduleMonthly}
     */
    CampaignScheduleMonthly,

    /**
     * The CampaignScheduleMonthlyEnd model constructor.
     * @property {module:model/CampaignScheduleMonthlyEnd}
     */
    CampaignScheduleMonthlyEnd,

    /**
     * The CampaignScheduleMonthlyStart model constructor.
     * @property {module:model/CampaignScheduleMonthlyStart}
     */
    CampaignScheduleMonthlyStart,

    /**
     * The CampaignScheduleOneshot model constructor.
     * @property {module:model/CampaignScheduleOneshot}
     */
    CampaignScheduleOneshot,

    /**
     * The CampaignScheduleWeekly model constructor.
     * @property {module:model/CampaignScheduleWeekly}
     */
    CampaignScheduleWeekly,

    /**
     * The CampaignScheduleWeeklyEnd model constructor.
     * @property {module:model/CampaignScheduleWeeklyEnd}
     */
    CampaignScheduleWeeklyEnd,

    /**
     * The CampaignScheduleWeeklyStart model constructor.
     * @property {module:model/CampaignScheduleWeeklyStart}
     */
    CampaignScheduleWeeklyStart,

    /**
     * The CampaignSoftwareUpdate model constructor.
     * @property {module:model/CampaignSoftwareUpdate}
     */
    CampaignSoftwareUpdate,

    /**
     * The CampaignSoftwareUpdateSoftwareUpdateInner model constructor.
     * @property {module:model/CampaignSoftwareUpdateSoftwareUpdateInner}
     */
    CampaignSoftwareUpdateSoftwareUpdateInner,

    /**
     * The CampaignStatusArchived model constructor.
     * @property {module:model/CampaignStatusArchived}
     */
    CampaignStatusArchived,

    /**
     * The CampaignStatusDisabled model constructor.
     * @property {module:model/CampaignStatusDisabled}
     */
    CampaignStatusDisabled,

    /**
     * The CampaignStatusEnabled model constructor.
     * @property {module:model/CampaignStatusEnabled}
     */
    CampaignStatusEnabled,

    /**
     * The CampaignSystemUpdate model constructor.
     * @property {module:model/CampaignSystemUpdate}
     */
    CampaignSystemUpdate,

    /**
     * The CategoriesTree model constructor.
     * @property {module:model/CategoriesTree}
     */
    CategoriesTree,

    /**
     * The ChangePendingNodeStatus200Response model constructor.
     * @property {module:model/ChangePendingNodeStatus200Response}
     */
    ChangePendingNodeStatus200Response,

    /**
     * The ChangePendingNodeStatus200ResponseData model constructor.
     * @property {module:model/ChangePendingNodeStatus200ResponseData}
     */
    ChangePendingNodeStatus200ResponseData,

    /**
     * The ChangePendingNodeStatusRequest model constructor.
     * @property {module:model/ChangePendingNodeStatusRequest}
     */
    ChangePendingNodeStatusRequest,

    /**
     * The ChangeRequest model constructor.
     * @property {module:model/ChangeRequest}
     */
    ChangeRequest,

    /**
     * The ChangeRequestChanges model constructor.
     * @property {module:model/ChangeRequestChanges}
     */
    ChangeRequestChanges,

    /**
     * The ChangeRequestChangesRulesInner model constructor.
     * @property {module:model/ChangeRequestChangesRulesInner}
     */
    ChangeRequestChangesRulesInner,

    /**
     * The ChangeRequestDetails200Response model constructor.
     * @property {module:model/ChangeRequestDetails200Response}
     */
    ChangeRequestDetails200Response,

    /**
     * The Check model constructor.
     * @property {module:model/Check}
     */
    Check,

    /**
     * The CheckCVE200Response model constructor.
     * @property {module:model/CheckCVE200Response}
     */
    CheckCVE200Response,

    /**
     * The CheckCVE200ResponseData model constructor.
     * @property {module:model/CheckCVE200ResponseData}
     */
    CheckCVE200ResponseData,

    /**
     * The CheckDirective200Response model constructor.
     * @property {module:model/CheckDirective200Response}
     */
    CheckDirective200Response,

    /**
     * The Color model constructor.
     * @property {module:model/Color}
     */
    Color,

    /**
     * The ComplianceDirectiveId model constructor.
     * @property {module:model/ComplianceDirectiveId}
     */
    ComplianceDirectiveId,

    /**
     * The ComplianceDirectiveIdData model constructor.
     * @property {module:model/ComplianceDirectiveIdData}
     */
    ComplianceDirectiveIdData,

    /**
     * The CreateArchive200Response model constructor.
     * @property {module:model/CreateArchive200Response}
     */
    CreateArchive200Response,

    /**
     * The CreateArchive200ResponseData model constructor.
     * @property {module:model/CreateArchive200ResponseData}
     */
    CreateArchive200ResponseData,

    /**
     * The CreateDataSource200Response model constructor.
     * @property {module:model/CreateDataSource200Response}
     */
    CreateDataSource200Response,

    /**
     * The CreateDataSource200ResponseData model constructor.
     * @property {module:model/CreateDataSource200ResponseData}
     */
    CreateDataSource200ResponseData,

    /**
     * The CreateDirective200Response model constructor.
     * @property {module:model/CreateDirective200Response}
     */
    CreateDirective200Response,

    /**
     * The CreateGroup200Response model constructor.
     * @property {module:model/CreateGroup200Response}
     */
    CreateGroup200Response,

    /**
     * The CreateGroupCategory200Response model constructor.
     * @property {module:model/CreateGroupCategory200Response}
     */
    CreateGroupCategory200Response,

    /**
     * The CreateGroupCategory200ResponseData model constructor.
     * @property {module:model/CreateGroupCategory200ResponseData}
     */
    CreateGroupCategory200ResponseData,

    /**
     * The CreateNodes200Response model constructor.
     * @property {module:model/CreateNodes200Response}
     */
    CreateNodes200Response,

    /**
     * The CreateNodes200ResponseData model constructor.
     * @property {module:model/CreateNodes200ResponseData}
     */
    CreateNodes200ResponseData,

    /**
     * The CreateParameter200Response model constructor.
     * @property {module:model/CreateParameter200Response}
     */
    CreateParameter200Response,

    /**
     * The CreateRule200Response model constructor.
     * @property {module:model/CreateRule200Response}
     */
    CreateRule200Response,

    /**
     * The CreateRuleCategory200Response model constructor.
     * @property {module:model/CreateRuleCategory200Response}
     */
    CreateRuleCategory200Response,

    /**
     * The CreateRuleCategory200ResponseData model constructor.
     * @property {module:model/CreateRuleCategory200ResponseData}
     */
    CreateRuleCategory200ResponseData,

    /**
     * The CreateTechnique200Response model constructor.
     * @property {module:model/CreateTechnique200Response}
     */
    CreateTechnique200Response,

    /**
     * The CreateTechnique200ResponseData model constructor.
     * @property {module:model/CreateTechnique200ResponseData}
     */
    CreateTechnique200ResponseData,

    /**
     * The CreateTechnique200ResponseDataTechniques model constructor.
     * @property {module:model/CreateTechnique200ResponseDataTechniques}
     */
    CreateTechnique200ResponseDataTechniques,

    /**
     * The CveCheck model constructor.
     * @property {module:model/CveCheck}
     */
    CveCheck,

    /**
     * The CveCheckPackagesInner model constructor.
     * @property {module:model/CveCheckPackagesInner}
     */
    CveCheckPackagesInner,

    /**
     * The CveCheckScore model constructor.
     * @property {module:model/CveCheckScore}
     */
    CveCheckScore,

    /**
     * The CveDetails model constructor.
     * @property {module:model/CveDetails}
     */
    CveDetails,

    /**
     * The CveDetailsCvssv2 model constructor.
     * @property {module:model/CveDetailsCvssv2}
     */
    CveDetailsCvssv2,

    /**
     * The CveDetailsCvssv3 model constructor.
     * @property {module:model/CveDetailsCvssv3}
     */
    CveDetailsCvssv3,

    /**
     * The Datasource model constructor.
     * @property {module:model/Datasource}
     */
    Datasource,

    /**
     * The DatasourceRunParameters model constructor.
     * @property {module:model/DatasourceRunParameters}
     */
    DatasourceRunParameters,

    /**
     * The DatasourceRunParametersSchedule model constructor.
     * @property {module:model/DatasourceRunParametersSchedule}
     */
    DatasourceRunParametersSchedule,

    /**
     * The DatasourceType model constructor.
     * @property {module:model/DatasourceType}
     */
    DatasourceType,

    /**
     * The DatasourceTypeParameters model constructor.
     * @property {module:model/DatasourceTypeParameters}
     */
    DatasourceTypeParameters,

    /**
     * The DatasourceTypeParametersHeadersInner model constructor.
     * @property {module:model/DatasourceTypeParametersHeadersInner}
     */
    DatasourceTypeParametersHeadersInner,

    /**
     * The DatasourceTypeParametersRequestMode model constructor.
     * @property {module:model/DatasourceTypeParametersRequestMode}
     */
    DatasourceTypeParametersRequestMode,

    /**
     * The DeclineChangeRequest200Response model constructor.
     * @property {module:model/DeclineChangeRequest200Response}
     */
    DeclineChangeRequest200Response,

    /**
     * The DeleteCampaign200Response model constructor.
     * @property {module:model/DeleteCampaign200Response}
     */
    DeleteCampaign200Response,

    /**
     * The DeleteCampaignEvent200Response model constructor.
     * @property {module:model/DeleteCampaignEvent200Response}
     */
    DeleteCampaignEvent200Response,

    /**
     * The DeleteDataSource200Response model constructor.
     * @property {module:model/DeleteDataSource200Response}
     */
    DeleteDataSource200Response,

    /**
     * The DeleteDirective200Response model constructor.
     * @property {module:model/DeleteDirective200Response}
     */
    DeleteDirective200Response,

    /**
     * The DeleteGroup200Response model constructor.
     * @property {module:model/DeleteGroup200Response}
     */
    DeleteGroup200Response,

    /**
     * The DeleteGroupCategory200Response model constructor.
     * @property {module:model/DeleteGroupCategory200Response}
     */
    DeleteGroupCategory200Response,

    /**
     * The DeleteNode200Response model constructor.
     * @property {module:model/DeleteNode200Response}
     */
    DeleteNode200Response,

    /**
     * The DeleteParameter200Response model constructor.
     * @property {module:model/DeleteParameter200Response}
     */
    DeleteParameter200Response,

    /**
     * The DeleteParameter500Response model constructor.
     * @property {module:model/DeleteParameter500Response}
     */
    DeleteParameter500Response,

    /**
     * The DeleteRule200Response model constructor.
     * @property {module:model/DeleteRule200Response}
     */
    DeleteRule200Response,

    /**
     * The DeleteRuleCategory200Response model constructor.
     * @property {module:model/DeleteRuleCategory200Response}
     */
    DeleteRuleCategory200Response,

    /**
     * The DeleteRuleCategory200ResponseData model constructor.
     * @property {module:model/DeleteRuleCategory200ResponseData}
     */
    DeleteRuleCategory200ResponseData,

    /**
     * The DeleteSecret200Response model constructor.
     * @property {module:model/DeleteSecret200Response}
     */
    DeleteSecret200Response,

    /**
     * The DeleteTechnique200Response model constructor.
     * @property {module:model/DeleteTechnique200Response}
     */
    DeleteTechnique200Response,

    /**
     * The DeleteTechnique200ResponseData model constructor.
     * @property {module:model/DeleteTechnique200ResponseData}
     */
    DeleteTechnique200ResponseData,

    /**
     * The DeleteTechnique200ResponseDataTechniques model constructor.
     * @property {module:model/DeleteTechnique200ResponseDataTechniques}
     */
    DeleteTechnique200ResponseDataTechniques,

    /**
     * The DeleteUser200Response model constructor.
     * @property {module:model/DeleteUser200Response}
     */
    DeleteUser200Response,

    /**
     * The DeleteUser200ResponseData model constructor.
     * @property {module:model/DeleteUser200ResponseData}
     */
    DeleteUser200ResponseData,

    /**
     * The DeleteUser200ResponseDataDeletedUser model constructor.
     * @property {module:model/DeleteUser200ResponseDataDeletedUser}
     */
    DeleteUser200ResponseDataDeletedUser,

    /**
     * The DemoteToNode200Response model constructor.
     * @property {module:model/DemoteToNode200Response}
     */
    DemoteToNode200Response,

    /**
     * The Directive model constructor.
     * @property {module:model/Directive}
     */
    Directive,

    /**
     * The DirectiveDetails200Response model constructor.
     * @property {module:model/DirectiveDetails200Response}
     */
    DirectiveDetails200Response,

    /**
     * The DirectiveNew model constructor.
     * @property {module:model/DirectiveNew}
     */
    DirectiveNew,

    /**
     * The DirectiveNodeCompliance model constructor.
     * @property {module:model/DirectiveNodeCompliance}
     */
    DirectiveNodeCompliance,

    /**
     * The DirectiveNodeComplianceComplianceDetails model constructor.
     * @property {module:model/DirectiveNodeComplianceComplianceDetails}
     */
    DirectiveNodeComplianceComplianceDetails,

    /**
     * The DirectiveRuleCompliance model constructor.
     * @property {module:model/DirectiveRuleCompliance}
     */
    DirectiveRuleCompliance,

    /**
     * The DirectiveRuleComplianceComponentsInner model constructor.
     * @property {module:model/DirectiveRuleComplianceComponentsInner}
     */
    DirectiveRuleComplianceComponentsInner,

    /**
     * The DirectiveTagsInner model constructor.
     * @property {module:model/DirectiveTagsInner}
     */
    DirectiveTagsInner,

    /**
     * The EditorTechnique model constructor.
     * @property {module:model/EditorTechnique}
     */
    EditorTechnique,

    /**
     * The EditorTechniqueCallsInner model constructor.
     * @property {module:model/EditorTechniqueCallsInner}
     */
    EditorTechniqueCallsInner,

    /**
     * The FileWatcherRestart200Response model constructor.
     * @property {module:model/FileWatcherRestart200Response}
     */
    FileWatcherRestart200Response,

    /**
     * The FileWatcherStart200Response model constructor.
     * @property {module:model/FileWatcherStart200Response}
     */
    FileWatcherStart200Response,

    /**
     * The FileWatcherStop200Response model constructor.
     * @property {module:model/FileWatcherStop200Response}
     */
    FileWatcherStop200Response,

    /**
     * The GetAllCampaignEvents200Response model constructor.
     * @property {module:model/GetAllCampaignEvents200Response}
     */
    GetAllCampaignEvents200Response,

    /**
     * The GetAllCampaignEvents200ResponseData model constructor.
     * @property {module:model/GetAllCampaignEvents200ResponseData}
     */
    GetAllCampaignEvents200ResponseData,

    /**
     * The GetAllCve200Response model constructor.
     * @property {module:model/GetAllCve200Response}
     */
    GetAllCve200Response,

    /**
     * The GetAllCve200ResponseData model constructor.
     * @property {module:model/GetAllCve200ResponseData}
     */
    GetAllCve200ResponseData,

    /**
     * The GetAllDataSources200Response model constructor.
     * @property {module:model/GetAllDataSources200Response}
     */
    GetAllDataSources200Response,

    /**
     * The GetAllDataSources200ResponseData model constructor.
     * @property {module:model/GetAllDataSources200ResponseData}
     */
    GetAllDataSources200ResponseData,

    /**
     * The GetAllSecrets200Response model constructor.
     * @property {module:model/GetAllSecrets200Response}
     */
    GetAllSecrets200Response,

    /**
     * The GetAllSecrets200ResponseData model constructor.
     * @property {module:model/GetAllSecrets200ResponseData}
     */
    GetAllSecrets200ResponseData,

    /**
     * The GetAllSecrets200ResponseDataSecretsInner model constructor.
     * @property {module:model/GetAllSecrets200ResponseDataSecretsInner}
     */
    GetAllSecrets200ResponseDataSecretsInner,

    /**
     * The GetAllSettings200Response model constructor.
     * @property {module:model/GetAllSettings200Response}
     */
    GetAllSettings200Response,

    /**
     * The GetAllSettings200ResponseData model constructor.
     * @property {module:model/GetAllSettings200ResponseData}
     */
    GetAllSettings200ResponseData,

    /**
     * The GetAllSettings200ResponseDataSettings model constructor.
     * @property {module:model/GetAllSettings200ResponseDataSettings}
     */
    GetAllSettings200ResponseDataSettings,

    /**
     * The GetAllSettings200ResponseDataSettingsAllowedNetworksInner model constructor.
     * @property {module:model/GetAllSettings200ResponseDataSettingsAllowedNetworksInner}
     */
    GetAllSettings200ResponseDataSettingsAllowedNetworksInner,

    /**
     * The GetAllowedNetworks200Response model constructor.
     * @property {module:model/GetAllowedNetworks200Response}
     */
    GetAllowedNetworks200Response,

    /**
     * The GetAllowedNetworks200ResponseData model constructor.
     * @property {module:model/GetAllowedNetworks200ResponseData}
     */
    GetAllowedNetworks200ResponseData,

    /**
     * The GetAllowedNetworks200ResponseDataSettings model constructor.
     * @property {module:model/GetAllowedNetworks200ResponseDataSettings}
     */
    GetAllowedNetworks200ResponseDataSettings,

    /**
     * The GetBrandingConf200Response model constructor.
     * @property {module:model/GetBrandingConf200Response}
     */
    GetBrandingConf200Response,

    /**
     * The GetBrandingConf200ResponseData model constructor.
     * @property {module:model/GetBrandingConf200ResponseData}
     */
    GetBrandingConf200ResponseData,

    /**
     * The GetCVECheckConfiguration200Response model constructor.
     * @property {module:model/GetCVECheckConfiguration200Response}
     */
    GetCVECheckConfiguration200Response,

    /**
     * The GetCVECheckConfiguration200ResponseData model constructor.
     * @property {module:model/GetCVECheckConfiguration200ResponseData}
     */
    GetCVECheckConfiguration200ResponseData,

    /**
     * The GetCVEList200Response model constructor.
     * @property {module:model/GetCVEList200Response}
     */
    GetCVEList200Response,

    /**
     * The GetCVEListRequest model constructor.
     * @property {module:model/GetCVEListRequest}
     */
    GetCVEListRequest,

    /**
     * The GetCampaign200Response model constructor.
     * @property {module:model/GetCampaign200Response}
     */
    GetCampaign200Response,

    /**
     * The GetCampaignEventResult200Response model constructor.
     * @property {module:model/GetCampaignEventResult200Response}
     */
    GetCampaignEventResult200Response,

    /**
     * The GetCampaignEventResult200ResponseData model constructor.
     * @property {module:model/GetCampaignEventResult200ResponseData}
     */
    GetCampaignEventResult200ResponseData,

    /**
     * The GetCampaignEventResultForNode200Response model constructor.
     * @property {module:model/GetCampaignEventResultForNode200Response}
     */
    GetCampaignEventResultForNode200Response,

    /**
     * The GetCampaignEventResultForNode200ResponseData model constructor.
     * @property {module:model/GetCampaignEventResultForNode200ResponseData}
     */
    GetCampaignEventResultForNode200ResponseData,

    /**
     * The GetCampaignHistory200Response model constructor.
     * @property {module:model/GetCampaignHistory200Response}
     */
    GetCampaignHistory200Response,

    /**
     * The GetCampaignHistory200ResponseData model constructor.
     * @property {module:model/GetCampaignHistory200ResponseData}
     */
    GetCampaignHistory200ResponseData,

    /**
     * The GetCve200Response model constructor.
     * @property {module:model/GetCve200Response}
     */
    GetCve200Response,

    /**
     * The GetDataSource200Response model constructor.
     * @property {module:model/GetDataSource200Response}
     */
    GetDataSource200Response,

    /**
     * The GetDirectiveComplianceId200Response model constructor.
     * @property {module:model/GetDirectiveComplianceId200Response}
     */
    GetDirectiveComplianceId200Response,

    /**
     * The GetDirectivesCompliance200Response model constructor.
     * @property {module:model/GetDirectivesCompliance200Response}
     */
    GetDirectivesCompliance200Response,

    /**
     * The GetDirectivesCompliance200ResponseData model constructor.
     * @property {module:model/GetDirectivesCompliance200ResponseData}
     */
    GetDirectivesCompliance200ResponseData,

    /**
     * The GetDirectivesCompliance200ResponseDataDirectivesCompliance model constructor.
     * @property {module:model/GetDirectivesCompliance200ResponseDataDirectivesCompliance}
     */
    GetDirectivesCompliance200ResponseDataDirectivesCompliance,

    /**
     * The GetDirectivesCompliance200ResponseDataDirectivesComplianceComplianceDetails model constructor.
     * @property {module:model/GetDirectivesCompliance200ResponseDataDirectivesComplianceComplianceDetails}
     */
    GetDirectivesCompliance200ResponseDataDirectivesComplianceComplianceDetails,

    /**
     * The GetEventsCampaign200Response model constructor.
     * @property {module:model/GetEventsCampaign200Response}
     */
    GetEventsCampaign200Response,

    /**
     * The GetGlobalCompliance200Response model constructor.
     * @property {module:model/GetGlobalCompliance200Response}
     */
    GetGlobalCompliance200Response,

    /**
     * The GetGlobalCompliance200ResponseData model constructor.
     * @property {module:model/GetGlobalCompliance200ResponseData}
     */
    GetGlobalCompliance200ResponseData,

    /**
     * The GetGlobalCompliance200ResponseDataGlobalCompliance model constructor.
     * @property {module:model/GetGlobalCompliance200ResponseDataGlobalCompliance}
     */
    GetGlobalCompliance200ResponseDataGlobalCompliance,

    /**
     * The GetGlobalCompliance200ResponseDataGlobalComplianceComplianceDetails model constructor.
     * @property {module:model/GetGlobalCompliance200ResponseDataGlobalComplianceComplianceDetails}
     */
    GetGlobalCompliance200ResponseDataGlobalComplianceComplianceDetails,

    /**
     * The GetGroupCategoryDetails200Response model constructor.
     * @property {module:model/GetGroupCategoryDetails200Response}
     */
    GetGroupCategoryDetails200Response,

    /**
     * The GetGroupTree200Response model constructor.
     * @property {module:model/GetGroupTree200Response}
     */
    GetGroupTree200Response,

    /**
     * The GetGroupTree200ResponseData model constructor.
     * @property {module:model/GetGroupTree200ResponseData}
     */
    GetGroupTree200ResponseData,

    /**
     * The GetHealthcheckResult200Response model constructor.
     * @property {module:model/GetHealthcheckResult200Response}
     */
    GetHealthcheckResult200Response,

    /**
     * The GetLastCVECheck200Response model constructor.
     * @property {module:model/GetLastCVECheck200Response}
     */
    GetLastCVECheck200Response,

    /**
     * The GetLastCVECheck200ResponseData model constructor.
     * @property {module:model/GetLastCVECheck200ResponseData}
     */
    GetLastCVECheck200ResponseData,

    /**
     * The GetNodeCompliance200Response model constructor.
     * @property {module:model/GetNodeCompliance200Response}
     */
    GetNodeCompliance200Response,

    /**
     * The GetNodesCompliance200Response model constructor.
     * @property {module:model/GetNodesCompliance200Response}
     */
    GetNodesCompliance200Response,

    /**
     * The GetNodesCompliance200ResponseData model constructor.
     * @property {module:model/GetNodesCompliance200ResponseData}
     */
    GetNodesCompliance200ResponseData,

    /**
     * The GetNodesCompliance200ResponseDataNodesInner model constructor.
     * @property {module:model/GetNodesCompliance200ResponseDataNodesInner}
     */
    GetNodesCompliance200ResponseDataNodesInner,

    /**
     * The GetNodesStatus200Response model constructor.
     * @property {module:model/GetNodesStatus200Response}
     */
    GetNodesStatus200Response,

    /**
     * The GetNodesStatus200ResponseData model constructor.
     * @property {module:model/GetNodesStatus200ResponseData}
     */
    GetNodesStatus200ResponseData,

    /**
     * The GetNodesStatus200ResponseDataNodesInner model constructor.
     * @property {module:model/GetNodesStatus200ResponseDataNodesInner}
     */
    GetNodesStatus200ResponseDataNodesInner,

    /**
     * The GetRole200Response model constructor.
     * @property {module:model/GetRole200Response}
     */
    GetRole200Response,

    /**
     * The GetRole200ResponseDataInner model constructor.
     * @property {module:model/GetRole200ResponseDataInner}
     */
    GetRole200ResponseDataInner,

    /**
     * The GetRuleCategoryDetails200Response model constructor.
     * @property {module:model/GetRuleCategoryDetails200Response}
     */
    GetRuleCategoryDetails200Response,

    /**
     * The GetRuleCategoryDetails200ResponseData model constructor.
     * @property {module:model/GetRuleCategoryDetails200ResponseData}
     */
    GetRuleCategoryDetails200ResponseData,

    /**
     * The GetRuleCompliance200Response model constructor.
     * @property {module:model/GetRuleCompliance200Response}
     */
    GetRuleCompliance200Response,

    /**
     * The GetRuleTree200Response model constructor.
     * @property {module:model/GetRuleTree200Response}
     */
    GetRuleTree200Response,

    /**
     * The GetRuleTree200ResponseData model constructor.
     * @property {module:model/GetRuleTree200ResponseData}
     */
    GetRuleTree200ResponseData,

    /**
     * The GetRulesCompliance200Response model constructor.
     * @property {module:model/GetRulesCompliance200Response}
     */
    GetRulesCompliance200Response,

    /**
     * The GetRulesCompliance200ResponseData model constructor.
     * @property {module:model/GetRulesCompliance200ResponseData}
     */
    GetRulesCompliance200ResponseData,

    /**
     * The GetRulesCompliance200ResponseDataRulesInner model constructor.
     * @property {module:model/GetRulesCompliance200ResponseDataRulesInner}
     */
    GetRulesCompliance200ResponseDataRulesInner,

    /**
     * The GetSecret200Response model constructor.
     * @property {module:model/GetSecret200Response}
     */
    GetSecret200Response,

    /**
     * The GetSetting200Response model constructor.
     * @property {module:model/GetSetting200Response}
     */
    GetSetting200Response,

    /**
     * The GetSetting200ResponseData model constructor.
     * @property {module:model/GetSetting200ResponseData}
     */
    GetSetting200ResponseData,

    /**
     * The GetStatus200Response model constructor.
     * @property {module:model/GetStatus200Response}
     */
    GetStatus200Response,

    /**
     * The GetStatus200ResponseData model constructor.
     * @property {module:model/GetStatus200ResponseData}
     */
    GetStatus200ResponseData,

    /**
     * The GetSystemInfo200Response model constructor.
     * @property {module:model/GetSystemInfo200Response}
     */
    GetSystemInfo200Response,

    /**
     * The GetSystemInfo200ResponseData model constructor.
     * @property {module:model/GetSystemInfo200ResponseData}
     */
    GetSystemInfo200ResponseData,

    /**
     * The GetSystemInfo200ResponseDataRudder model constructor.
     * @property {module:model/GetSystemInfo200ResponseDataRudder}
     */
    GetSystemInfo200ResponseDataRudder,

    /**
     * The GetTechniqueAllVersion200Response model constructor.
     * @property {module:model/GetTechniqueAllVersion200Response}
     */
    GetTechniqueAllVersion200Response,

    /**
     * The GetTechniqueAllVersion200ResponseData model constructor.
     * @property {module:model/GetTechniqueAllVersion200ResponseData}
     */
    GetTechniqueAllVersion200ResponseData,

    /**
     * The GetTechniqueAllVersion200ResponseDataTechniquesInner model constructor.
     * @property {module:model/GetTechniqueAllVersion200ResponseDataTechniquesInner}
     */
    GetTechniqueAllVersion200ResponseDataTechniquesInner,

    /**
     * The GetTechniquesResources200Response model constructor.
     * @property {module:model/GetTechniquesResources200Response}
     */
    GetTechniquesResources200Response,

    /**
     * The GetTechniquesResources200ResponseData model constructor.
     * @property {module:model/GetTechniquesResources200ResponseData}
     */
    GetTechniquesResources200ResponseData,

    /**
     * The GetUserInfo200Response model constructor.
     * @property {module:model/GetUserInfo200Response}
     */
    GetUserInfo200Response,

    /**
     * The GetUserInfo200ResponseData model constructor.
     * @property {module:model/GetUserInfo200ResponseData}
     */
    GetUserInfo200ResponseData,

    /**
     * The Group model constructor.
     * @property {module:model/Group}
     */
    Group,

    /**
     * The GroupCategory model constructor.
     * @property {module:model/GroupCategory}
     */
    GroupCategory,

    /**
     * The GroupCategoryUpdate model constructor.
     * @property {module:model/GroupCategoryUpdate}
     */
    GroupCategoryUpdate,

    /**
     * The GroupDetails200Response model constructor.
     * @property {module:model/GroupDetails200Response}
     */
    GroupDetails200Response,

    /**
     * The GroupNew model constructor.
     * @property {module:model/GroupNew}
     */
    GroupNew,

    /**
     * The GroupNewQuery model constructor.
     * @property {module:model/GroupNewQuery}
     */
    GroupNewQuery,

    /**
     * The GroupPropertiesInner model constructor.
     * @property {module:model/GroupPropertiesInner}
     */
    GroupPropertiesInner,

    /**
     * The GroupQuery model constructor.
     * @property {module:model/GroupQuery}
     */
    GroupQuery,

    /**
     * The GroupQueryWhereInner model constructor.
     * @property {module:model/GroupQueryWhereInner}
     */
    GroupQueryWhereInner,

    /**
     * The GroupUpdate model constructor.
     * @property {module:model/GroupUpdate}
     */
    GroupUpdate,

    /**
     * The Import200Response model constructor.
     * @property {module:model/Import200Response}
     */
    Import200Response,

    /**
     * The Import200ResponseData model constructor.
     * @property {module:model/Import200ResponseData}
     */
    Import200ResponseData,

    /**
     * The ListAcceptedNodes200Response model constructor.
     * @property {module:model/ListAcceptedNodes200Response}
     */
    ListAcceptedNodes200Response,

    /**
     * The ListAcceptedNodes200ResponseData model constructor.
     * @property {module:model/ListAcceptedNodes200ResponseData}
     */
    ListAcceptedNodes200ResponseData,

    /**
     * The ListArchives200Response model constructor.
     * @property {module:model/ListArchives200Response}
     */
    ListArchives200Response,

    /**
     * The ListArchives200ResponseData model constructor.
     * @property {module:model/ListArchives200ResponseData}
     */
    ListArchives200ResponseData,

    /**
     * The ListArchives200ResponseDataFullInner model constructor.
     * @property {module:model/ListArchives200ResponseDataFullInner}
     */
    ListArchives200ResponseDataFullInner,

    /**
     * The ListChangeRequests200Response model constructor.
     * @property {module:model/ListChangeRequests200Response}
     */
    ListChangeRequests200Response,

    /**
     * The ListChangeRequests200ResponseData model constructor.
     * @property {module:model/ListChangeRequests200ResponseData}
     */
    ListChangeRequests200ResponseData,

    /**
     * The ListDirectives200Response model constructor.
     * @property {module:model/ListDirectives200Response}
     */
    ListDirectives200Response,

    /**
     * The ListDirectives200ResponseData model constructor.
     * @property {module:model/ListDirectives200ResponseData}
     */
    ListDirectives200ResponseData,

    /**
     * The ListGroups200Response model constructor.
     * @property {module:model/ListGroups200Response}
     */
    ListGroups200Response,

    /**
     * The ListGroups200ResponseData model constructor.
     * @property {module:model/ListGroups200ResponseData}
     */
    ListGroups200ResponseData,

    /**
     * The ListParameters200Response model constructor.
     * @property {module:model/ListParameters200Response}
     */
    ListParameters200Response,

    /**
     * The ListParameters200ResponseData model constructor.
     * @property {module:model/ListParameters200ResponseData}
     */
    ListParameters200ResponseData,

    /**
     * The ListPendingNodes200Response model constructor.
     * @property {module:model/ListPendingNodes200Response}
     */
    ListPendingNodes200Response,

    /**
     * The ListRules200Response model constructor.
     * @property {module:model/ListRules200Response}
     */
    ListRules200Response,

    /**
     * The ListRules200ResponseData model constructor.
     * @property {module:model/ListRules200ResponseData}
     */
    ListRules200ResponseData,

    /**
     * The ListTechniqueVersionDirectives200Response model constructor.
     * @property {module:model/ListTechniqueVersionDirectives200Response}
     */
    ListTechniqueVersionDirectives200Response,

    /**
     * The ListTechniques200Response model constructor.
     * @property {module:model/ListTechniques200Response}
     */
    ListTechniques200Response,

    /**
     * The ListTechniques200ResponseData model constructor.
     * @property {module:model/ListTechniques200ResponseData}
     */
    ListTechniques200ResponseData,

    /**
     * The ListTechniquesDirectives200Response model constructor.
     * @property {module:model/ListTechniquesDirectives200Response}
     */
    ListTechniquesDirectives200Response,

    /**
     * The ListTechniquesVersions200Response model constructor.
     * @property {module:model/ListTechniquesVersions200Response}
     */
    ListTechniquesVersions200Response,

    /**
     * The ListTechniquesVersions200ResponseData model constructor.
     * @property {module:model/ListTechniquesVersions200ResponseData}
     */
    ListTechniquesVersions200ResponseData,

    /**
     * The ListUsers200Response model constructor.
     * @property {module:model/ListUsers200Response}
     */
    ListUsers200Response,

    /**
     * The Logo model constructor.
     * @property {module:model/Logo}
     */
    Logo,

    /**
     * The MethodParameter model constructor.
     * @property {module:model/MethodParameter}
     */
    MethodParameter,

    /**
     * The MethodParameterConstraints model constructor.
     * @property {module:model/MethodParameterConstraints}
     */
    MethodParameterConstraints,

    /**
     * The Methods model constructor.
     * @property {module:model/Methods}
     */
    Methods,

    /**
     * The Methods200Response model constructor.
     * @property {module:model/Methods200Response}
     */
    Methods200Response,

    /**
     * The Methods200ResponseData model constructor.
     * @property {module:model/Methods200ResponseData}
     */
    Methods200ResponseData,

    /**
     * The MethodsCondition model constructor.
     * @property {module:model/MethodsCondition}
     */
    MethodsCondition,

    /**
     * The MethodsDeprecated model constructor.
     * @property {module:model/MethodsDeprecated}
     */
    MethodsDeprecated,

    /**
     * The ModifyAllowedNetworks200Response model constructor.
     * @property {module:model/ModifyAllowedNetworks200Response}
     */
    ModifyAllowedNetworks200Response,

    /**
     * The ModifyAllowedNetworks200ResponseData model constructor.
     * @property {module:model/ModifyAllowedNetworks200ResponseData}
     */
    ModifyAllowedNetworks200ResponseData,

    /**
     * The ModifyAllowedNetworksRequest model constructor.
     * @property {module:model/ModifyAllowedNetworksRequest}
     */
    ModifyAllowedNetworksRequest,

    /**
     * The ModifyAllowedNetworksRequestAllowedNetworks model constructor.
     * @property {module:model/ModifyAllowedNetworksRequestAllowedNetworks}
     */
    ModifyAllowedNetworksRequestAllowedNetworks,

    /**
     * The ModifySetting200Response model constructor.
     * @property {module:model/ModifySetting200Response}
     */
    ModifySetting200Response,

    /**
     * The ModifySettingRequest model constructor.
     * @property {module:model/ModifySettingRequest}
     */
    ModifySettingRequest,

    /**
     * The NodeAddInner model constructor.
     * @property {module:model/NodeAddInner}
     */
    NodeAddInner,

    /**
     * The NodeAddInnerPropertiesInner model constructor.
     * @property {module:model/NodeAddInnerPropertiesInner}
     */
    NodeAddInnerPropertiesInner,

    /**
     * The NodeComplianceComponent model constructor.
     * @property {module:model/NodeComplianceComponent}
     */
    NodeComplianceComponent,

    /**
     * The NodeComplianceComponentValuesInner model constructor.
     * @property {module:model/NodeComplianceComponentValuesInner}
     */
    NodeComplianceComponentValuesInner,

    /**
     * The NodeComplianceComponentValuesInnerReportsInner model constructor.
     * @property {module:model/NodeComplianceComponentValuesInnerReportsInner}
     */
    NodeComplianceComponentValuesInnerReportsInner,

    /**
     * The NodeDetails200Response model constructor.
     * @property {module:model/NodeDetails200Response}
     */
    NodeDetails200Response,

    /**
     * The NodeFull model constructor.
     * @property {module:model/NodeFull}
     */
    NodeFull,

    /**
     * The NodeFullBios model constructor.
     * @property {module:model/NodeFullBios}
     */
    NodeFullBios,

    /**
     * The NodeFullControllersInner model constructor.
     * @property {module:model/NodeFullControllersInner}
     */
    NodeFullControllersInner,

    /**
     * The NodeFullEnvironmentVariablesInner model constructor.
     * @property {module:model/NodeFullEnvironmentVariablesInner}
     */
    NodeFullEnvironmentVariablesInner,

    /**
     * The NodeFullFileSystemsInner model constructor.
     * @property {module:model/NodeFullFileSystemsInner}
     */
    NodeFullFileSystemsInner,

    /**
     * The NodeFullMachine model constructor.
     * @property {module:model/NodeFullMachine}
     */
    NodeFullMachine,

    /**
     * The NodeFullManagementTechnologyDetails model constructor.
     * @property {module:model/NodeFullManagementTechnologyDetails}
     */
    NodeFullManagementTechnologyDetails,

    /**
     * The NodeFullManagementTechnologyInner model constructor.
     * @property {module:model/NodeFullManagementTechnologyInner}
     */
    NodeFullManagementTechnologyInner,

    /**
     * The NodeFullMemoriesInner model constructor.
     * @property {module:model/NodeFullMemoriesInner}
     */
    NodeFullMemoriesInner,

    /**
     * The NodeFullNetworkInterfacesInner model constructor.
     * @property {module:model/NodeFullNetworkInterfacesInner}
     */
    NodeFullNetworkInterfacesInner,

    /**
     * The NodeFullOs model constructor.
     * @property {module:model/NodeFullOs}
     */
    NodeFullOs,

    /**
     * The NodeFullPortsInner model constructor.
     * @property {module:model/NodeFullPortsInner}
     */
    NodeFullPortsInner,

    /**
     * The NodeFullProcessesInner model constructor.
     * @property {module:model/NodeFullProcessesInner}
     */
    NodeFullProcessesInner,

    /**
     * The NodeFullProcessorsInner model constructor.
     * @property {module:model/NodeFullProcessorsInner}
     */
    NodeFullProcessorsInner,

    /**
     * The NodeFullSlotsInner model constructor.
     * @property {module:model/NodeFullSlotsInner}
     */
    NodeFullSlotsInner,

    /**
     * The NodeFullSoftwareInner model constructor.
     * @property {module:model/NodeFullSoftwareInner}
     */
    NodeFullSoftwareInner,

    /**
     * The NodeFullSoftwareInnerLicense model constructor.
     * @property {module:model/NodeFullSoftwareInnerLicense}
     */
    NodeFullSoftwareInnerLicense,

    /**
     * The NodeFullSoftwareUpdateInner model constructor.
     * @property {module:model/NodeFullSoftwareUpdateInner}
     */
    NodeFullSoftwareUpdateInner,

    /**
     * The NodeFullSoundInner model constructor.
     * @property {module:model/NodeFullSoundInner}
     */
    NodeFullSoundInner,

    /**
     * The NodeFullStorageInner model constructor.
     * @property {module:model/NodeFullStorageInner}
     */
    NodeFullStorageInner,

    /**
     * The NodeFullTimezone model constructor.
     * @property {module:model/NodeFullTimezone}
     */
    NodeFullTimezone,

    /**
     * The NodeFullVideosInner model constructor.
     * @property {module:model/NodeFullVideosInner}
     */
    NodeFullVideosInner,

    /**
     * The NodeFullVirtualMachinesInner model constructor.
     * @property {module:model/NodeFullVirtualMachinesInner}
     */
    NodeFullVirtualMachinesInner,

    /**
     * The NodeInheritedProperties model constructor.
     * @property {module:model/NodeInheritedProperties}
     */
    NodeInheritedProperties,

    /**
     * The NodeInheritedProperties200Response model constructor.
     * @property {module:model/NodeInheritedProperties200Response}
     */
    NodeInheritedProperties200Response,

    /**
     * The NodeInheritedPropertiesPropertiesInner model constructor.
     * @property {module:model/NodeInheritedPropertiesPropertiesInner}
     */
    NodeInheritedPropertiesPropertiesInner,

    /**
     * The NodeInheritedPropertiesPropertiesInnerHierarchyInner model constructor.
     * @property {module:model/NodeInheritedPropertiesPropertiesInnerHierarchyInner}
     */
    NodeInheritedPropertiesPropertiesInnerHierarchyInner,

    /**
     * The NodeSettings model constructor.
     * @property {module:model/NodeSettings}
     */
    NodeSettings,

    /**
     * The Os model constructor.
     * @property {module:model/Os}
     */
    Os,

    /**
     * The Parameter model constructor.
     * @property {module:model/Parameter}
     */
    Parameter,

    /**
     * The ParameterDetails200Response model constructor.
     * @property {module:model/ParameterDetails200Response}
     */
    ParameterDetails200Response,

    /**
     * The PromoteToRelay200Response model constructor.
     * @property {module:model/PromoteToRelay200Response}
     */
    PromoteToRelay200Response,

    /**
     * The PurgeSoftware200Response model constructor.
     * @property {module:model/PurgeSoftware200Response}
     */
    PurgeSoftware200Response,

    /**
     * The QueueInformation200Response model constructor.
     * @property {module:model/QueueInformation200Response}
     */
    QueueInformation200Response,

    /**
     * The QueueInformation200ResponseData model constructor.
     * @property {module:model/QueueInformation200ResponseData}
     */
    QueueInformation200ResponseData,

    /**
     * The ReadCVEfromFS200Response model constructor.
     * @property {module:model/ReadCVEfromFS200Response}
     */
    ReadCVEfromFS200Response,

    /**
     * The RegeneratePolicies200Response model constructor.
     * @property {module:model/RegeneratePolicies200Response}
     */
    RegeneratePolicies200Response,

    /**
     * The RegeneratePolicies200ResponseData model constructor.
     * @property {module:model/RegeneratePolicies200ResponseData}
     */
    RegeneratePolicies200ResponseData,

    /**
     * The ReloadAll200Response model constructor.
     * @property {module:model/ReloadAll200Response}
     */
    ReloadAll200Response,

    /**
     * The ReloadAll200ResponseData model constructor.
     * @property {module:model/ReloadAll200ResponseData}
     */
    ReloadAll200ResponseData,

    /**
     * The ReloadAllDatasourcesAllNodes200Response model constructor.
     * @property {module:model/ReloadAllDatasourcesAllNodes200Response}
     */
    ReloadAllDatasourcesAllNodes200Response,

    /**
     * The ReloadAllDatasourcesOneNode200Response model constructor.
     * @property {module:model/ReloadAllDatasourcesOneNode200Response}
     */
    ReloadAllDatasourcesOneNode200Response,

    /**
     * The ReloadGroup200Response model constructor.
     * @property {module:model/ReloadGroup200Response}
     */
    ReloadGroup200Response,

    /**
     * The ReloadGroups200Response model constructor.
     * @property {module:model/ReloadGroups200Response}
     */
    ReloadGroups200Response,

    /**
     * The ReloadGroups200ResponseData model constructor.
     * @property {module:model/ReloadGroups200ResponseData}
     */
    ReloadGroups200ResponseData,

    /**
     * The ReloadOneDatasourceAllNodes200Response model constructor.
     * @property {module:model/ReloadOneDatasourceAllNodes200Response}
     */
    ReloadOneDatasourceAllNodes200Response,

    /**
     * The ReloadOneDatasourceOneNode200Response model constructor.
     * @property {module:model/ReloadOneDatasourceOneNode200Response}
     */
    ReloadOneDatasourceOneNode200Response,

    /**
     * The ReloadTechniques200Response model constructor.
     * @property {module:model/ReloadTechniques200Response}
     */
    ReloadTechniques200Response,

    /**
     * The ReloadTechniques200ResponseData model constructor.
     * @property {module:model/ReloadTechniques200ResponseData}
     */
    ReloadTechniques200ResponseData,

    /**
     * The ReloadUserConf200Response model constructor.
     * @property {module:model/ReloadUserConf200Response}
     */
    ReloadUserConf200Response,

    /**
     * The ReloadUserConf200ResponseData model constructor.
     * @property {module:model/ReloadUserConf200ResponseData}
     */
    ReloadUserConf200ResponseData,

    /**
     * The ReloadUserConf200ResponseDataReload model constructor.
     * @property {module:model/ReloadUserConf200ResponseDataReload}
     */
    ReloadUserConf200ResponseDataReload,

    /**
     * The RemoveValidatedUser200Response model constructor.
     * @property {module:model/RemoveValidatedUser200Response}
     */
    RemoveValidatedUser200Response,

    /**
     * The RestoreArchive200Response model constructor.
     * @property {module:model/RestoreArchive200Response}
     */
    RestoreArchive200Response,

    /**
     * The RestoreArchive200ResponseData model constructor.
     * @property {module:model/RestoreArchive200ResponseData}
     */
    RestoreArchive200ResponseData,

    /**
     * The Rule model constructor.
     * @property {module:model/Rule}
     */
    Rule,

    /**
     * The RuleCategory model constructor.
     * @property {module:model/RuleCategory}
     */
    RuleCategory,

    /**
     * The RuleCategoryUpdate model constructor.
     * @property {module:model/RuleCategoryUpdate}
     */
    RuleCategoryUpdate,

    /**
     * The RuleComplianceComponent model constructor.
     * @property {module:model/RuleComplianceComponent}
     */
    RuleComplianceComponent,

    /**
     * The RuleComplianceComponentComplianceDetails model constructor.
     * @property {module:model/RuleComplianceComponentComplianceDetails}
     */
    RuleComplianceComponentComplianceDetails,

    /**
     * The RuleComplianceComponentComponentsInner model constructor.
     * @property {module:model/RuleComplianceComponentComponentsInner}
     */
    RuleComplianceComponentComponentsInner,

    /**
     * The RuleComplianceComponentComponentsInnerValuesInner model constructor.
     * @property {module:model/RuleComplianceComponentComponentsInnerValuesInner}
     */
    RuleComplianceComponentComponentsInnerValuesInner,

    /**
     * The RuleComplianceComponentComponentsInnerValuesInnerReportsInner model constructor.
     * @property {module:model/RuleComplianceComponentComponentsInnerValuesInnerReportsInner}
     */
    RuleComplianceComponentComponentsInnerValuesInnerReportsInner,

    /**
     * The RuleDetails200Response model constructor.
     * @property {module:model/RuleDetails200Response}
     */
    RuleDetails200Response,

    /**
     * The RuleNew model constructor.
     * @property {module:model/RuleNew}
     */
    RuleNew,

    /**
     * The RuleTarget model constructor.
     * @property {module:model/RuleTarget}
     */
    RuleTarget,

    /**
     * The RuleTargetsInner model constructor.
     * @property {module:model/RuleTargetsInner}
     */
    RuleTargetsInner,

    /**
     * The RuleTargetsInnerExclude model constructor.
     * @property {module:model/RuleTargetsInnerExclude}
     */
    RuleTargetsInnerExclude,

    /**
     * The RuleTargetsInnerInclude model constructor.
     * @property {module:model/RuleTargetsInnerInclude}
     */
    RuleTargetsInnerInclude,

    /**
     * The RuleWithCategory model constructor.
     * @property {module:model/RuleWithCategory}
     */
    RuleWithCategory,

    /**
     * The SaveCampaign200Response model constructor.
     * @property {module:model/SaveCampaign200Response}
     */
    SaveCampaign200Response,

    /**
     * The SaveCampaignEvent200Response model constructor.
     * @property {module:model/SaveCampaignEvent200Response}
     */
    SaveCampaignEvent200Response,

    /**
     * The SaveWorkflowUser200Response model constructor.
     * @property {module:model/SaveWorkflowUser200Response}
     */
    SaveWorkflowUser200Response,

    /**
     * The SaveWorkflowUserRequest model constructor.
     * @property {module:model/SaveWorkflowUserRequest}
     */
    SaveWorkflowUserRequest,

    /**
     * The ScheduleCampaign200Response model constructor.
     * @property {module:model/ScheduleCampaign200Response}
     */
    ScheduleCampaign200Response,

    /**
     * The Secrets model constructor.
     * @property {module:model/Secrets}
     */
    Secrets,

    /**
     * The SetAllowedNetworks200Response model constructor.
     * @property {module:model/SetAllowedNetworks200Response}
     */
    SetAllowedNetworks200Response,

    /**
     * The SetAllowedNetworks200ResponseData model constructor.
     * @property {module:model/SetAllowedNetworks200ResponseData}
     */
    SetAllowedNetworks200ResponseData,

    /**
     * The SetAllowedNetworksRequest model constructor.
     * @property {module:model/SetAllowedNetworksRequest}
     */
    SetAllowedNetworksRequest,

    /**
     * The TechniqueBlock model constructor.
     * @property {module:model/TechniqueBlock}
     */
    TechniqueBlock,

    /**
     * The TechniqueBlockReportingLogic model constructor.
     * @property {module:model/TechniqueBlockReportingLogic}
     */
    TechniqueBlockReportingLogic,

    /**
     * The TechniqueCategories200Response model constructor.
     * @property {module:model/TechniqueCategories200Response}
     */
    TechniqueCategories200Response,

    /**
     * The TechniqueCategories200ResponseData model constructor.
     * @property {module:model/TechniqueCategories200ResponseData}
     */
    TechniqueCategories200ResponseData,

    /**
     * The TechniqueCategory model constructor.
     * @property {module:model/TechniqueCategory}
     */
    TechniqueCategory,

    /**
     * The TechniqueMethodCall model constructor.
     * @property {module:model/TechniqueMethodCall}
     */
    TechniqueMethodCall,

    /**
     * The TechniqueMethodCallParametersInner model constructor.
     * @property {module:model/TechniqueMethodCallParametersInner}
     */
    TechniqueMethodCallParametersInner,

    /**
     * The TechniqueParameter model constructor.
     * @property {module:model/TechniqueParameter}
     */
    TechniqueParameter,

    /**
     * The TechniqueResource model constructor.
     * @property {module:model/TechniqueResource}
     */
    TechniqueResource,

    /**
     * The TechniqueRevisions200Response model constructor.
     * @property {module:model/TechniqueRevisions200Response}
     */
    TechniqueRevisions200Response,

    /**
     * The TechniqueRevisions200ResponseData model constructor.
     * @property {module:model/TechniqueRevisions200ResponseData}
     */
    TechniqueRevisions200ResponseData,

    /**
     * The TechniquesResourcesInner model constructor.
     * @property {module:model/TechniquesResourcesInner}
     */
    TechniquesResourcesInner,

    /**
     * The TechniquesRevisionsInner model constructor.
     * @property {module:model/TechniquesRevisionsInner}
     */
    TechniquesRevisionsInner,

    /**
     * The TechniquesVersionsInner model constructor.
     * @property {module:model/TechniquesVersionsInner}
     */
    TechniquesVersionsInner,

    /**
     * The Timezone model constructor.
     * @property {module:model/Timezone}
     */
    Timezone,

    /**
     * The UpdateBRandingConf200Response model constructor.
     * @property {module:model/UpdateBRandingConf200Response}
     */
    UpdateBRandingConf200Response,

    /**
     * The UpdateCVE200Response model constructor.
     * @property {module:model/UpdateCVE200Response}
     */
    UpdateCVE200Response,

    /**
     * The UpdateCVE200ResponseData model constructor.
     * @property {module:model/UpdateCVE200ResponseData}
     */
    UpdateCVE200ResponseData,

    /**
     * The UpdateCVECheckConfiguration200Response model constructor.
     * @property {module:model/UpdateCVECheckConfiguration200Response}
     */
    UpdateCVECheckConfiguration200Response,

    /**
     * The UpdateCVECheckConfigurationRequest model constructor.
     * @property {module:model/UpdateCVECheckConfigurationRequest}
     */
    UpdateCVECheckConfigurationRequest,

    /**
     * The UpdateCVERequest model constructor.
     * @property {module:model/UpdateCVERequest}
     */
    UpdateCVERequest,

    /**
     * The UpdateChangeRequest200Response model constructor.
     * @property {module:model/UpdateChangeRequest200Response}
     */
    UpdateChangeRequest200Response,

    /**
     * The UpdateChangeRequestRequest model constructor.
     * @property {module:model/UpdateChangeRequestRequest}
     */
    UpdateChangeRequestRequest,

    /**
     * The UpdateDataSource200Response model constructor.
     * @property {module:model/UpdateDataSource200Response}
     */
    UpdateDataSource200Response,

    /**
     * The UpdateDirective200Response model constructor.
     * @property {module:model/UpdateDirective200Response}
     */
    UpdateDirective200Response,

    /**
     * The UpdateGroup200Response model constructor.
     * @property {module:model/UpdateGroup200Response}
     */
    UpdateGroup200Response,

    /**
     * The UpdateGroupCategory200Response model constructor.
     * @property {module:model/UpdateGroupCategory200Response}
     */
    UpdateGroupCategory200Response,

    /**
     * The UpdateNode200Response model constructor.
     * @property {module:model/UpdateNode200Response}
     */
    UpdateNode200Response,

    /**
     * The UpdateParameter200Response model constructor.
     * @property {module:model/UpdateParameter200Response}
     */
    UpdateParameter200Response,

    /**
     * The UpdatePolicies200Response model constructor.
     * @property {module:model/UpdatePolicies200Response}
     */
    UpdatePolicies200Response,

    /**
     * The UpdateRule200Response model constructor.
     * @property {module:model/UpdateRule200Response}
     */
    UpdateRule200Response,

    /**
     * The UpdateRule200ResponseData model constructor.
     * @property {module:model/UpdateRule200ResponseData}
     */
    UpdateRule200ResponseData,

    /**
     * The UpdateRuleCategory200Response model constructor.
     * @property {module:model/UpdateRuleCategory200Response}
     */
    UpdateRuleCategory200Response,

    /**
     * The UpdateSecret200Response model constructor.
     * @property {module:model/UpdateSecret200Response}
     */
    UpdateSecret200Response,

    /**
     * The UpdateUser200Response model constructor.
     * @property {module:model/UpdateUser200Response}
     */
    UpdateUser200Response,

    /**
     * The UpdateUser200ResponseData model constructor.
     * @property {module:model/UpdateUser200ResponseData}
     */
    UpdateUser200ResponseData,

    /**
     * The UpdateUser200ResponseDataUpdatedUser model constructor.
     * @property {module:model/UpdateUser200ResponseDataUpdatedUser}
     */
    UpdateUser200ResponseDataUpdatedUser,

    /**
     * The UploadInventory200Response model constructor.
     * @property {module:model/UploadInventory200Response}
     */
    UploadInventory200Response,

    /**
     * The Users model constructor.
     * @property {module:model/Users}
     */
    Users,

    /**
     * The ValidatedUser model constructor.
     * @property {module:model/ValidatedUser}
     */
    ValidatedUser,

    /**
    * The APIInfoApi service constructor.
    * @property {module:api/APIInfoApi}
    */
    APIInfoApi,

    /**
    * The ArchivesApi service constructor.
    * @property {module:api/ArchivesApi}
    */
    ArchivesApi,

    /**
    * The BrandingApi service constructor.
    * @property {module:api/BrandingApi}
    */
    BrandingApi,

    /**
    * The CVEApi service constructor.
    * @property {module:api/CVEApi}
    */
    CVEApi,

    /**
    * The CampaignsApi service constructor.
    * @property {module:api/CampaignsApi}
    */
    CampaignsApi,

    /**
    * The ChangeRequestsApi service constructor.
    * @property {module:api/ChangeRequestsApi}
    */
    ChangeRequestsApi,

    /**
    * The ComplianceApi service constructor.
    * @property {module:api/ComplianceApi}
    */
    ComplianceApi,

    /**
    * The DataSourcesApi service constructor.
    * @property {module:api/DataSourcesApi}
    */
    DataSourcesApi,

    /**
    * The DirectivesApi service constructor.
    * @property {module:api/DirectivesApi}
    */
    DirectivesApi,

    /**
    * The GroupsApi service constructor.
    * @property {module:api/GroupsApi}
    */
    GroupsApi,

    /**
    * The InventoriesApi service constructor.
    * @property {module:api/InventoriesApi}
    */
    InventoriesApi,

    /**
    * The NodesApi service constructor.
    * @property {module:api/NodesApi}
    */
    NodesApi,

    /**
    * The ParametersApi service constructor.
    * @property {module:api/ParametersApi}
    */
    ParametersApi,

    /**
    * The RulesApi service constructor.
    * @property {module:api/RulesApi}
    */
    RulesApi,

    /**
    * The ScaleOutRelayApi service constructor.
    * @property {module:api/ScaleOutRelayApi}
    */
    ScaleOutRelayApi,

    /**
    * The SecretManagementApi service constructor.
    * @property {module:api/SecretManagementApi}
    */
    SecretManagementApi,

    /**
    * The SettingsApi service constructor.
    * @property {module:api/SettingsApi}
    */
    SettingsApi,

    /**
    * The StatusApi service constructor.
    * @property {module:api/StatusApi}
    */
    StatusApi,

    /**
    * The SystemApi service constructor.
    * @property {module:api/SystemApi}
    */
    SystemApi,

    /**
    * The SystemUpdateCampaignsApi service constructor.
    * @property {module:api/SystemUpdateCampaignsApi}
    */
    SystemUpdateCampaignsApi,

    /**
    * The TechniquesApi service constructor.
    * @property {module:api/TechniquesApi}
    */
    TechniquesApi,

    /**
    * The UserManagementApi service constructor.
    * @property {module:api/UserManagementApi}
    */
    UserManagementApi
};
