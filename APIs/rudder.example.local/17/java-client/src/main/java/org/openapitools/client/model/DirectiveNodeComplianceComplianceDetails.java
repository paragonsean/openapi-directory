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

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.Arrays;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;
import com.google.gson.TypeAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * DirectiveNodeComplianceComplianceDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:58.781092-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DirectiveNodeComplianceComplianceDetails {
  public static final String SERIALIZED_NAME_ERROR = "error";
  @SerializedName(SERIALIZED_NAME_ERROR)
  private Float error;

  public static final String SERIALIZED_NAME_NO_REPORT = "noReport";
  @SerializedName(SERIALIZED_NAME_NO_REPORT)
  private Float noReport;

  public static final String SERIALIZED_NAME_SUCCESS_ALREADY_O_K = "successAlreadyOK";
  @SerializedName(SERIALIZED_NAME_SUCCESS_ALREADY_O_K)
  private Float successAlreadyOK;

  public static final String SERIALIZED_NAME_SUCCESS_NOT_APPLICABLE = "successNotApplicable";
  @SerializedName(SERIALIZED_NAME_SUCCESS_NOT_APPLICABLE)
  private Float successNotApplicable;

  public static final String SERIALIZED_NAME_SUCCESS_REPAIRED = "successRepaired";
  @SerializedName(SERIALIZED_NAME_SUCCESS_REPAIRED)
  private Float successRepaired;

  public static final String SERIALIZED_NAME_UNEXPECTED_MISSING_COMPONENT = "unexpectedMissingComponent";
  @SerializedName(SERIALIZED_NAME_UNEXPECTED_MISSING_COMPONENT)
  private Float unexpectedMissingComponent;

  public static final String SERIALIZED_NAME_UNEXPECTED_UNKNOWN_COMPONENT = "unexpectedUnknownComponent";
  @SerializedName(SERIALIZED_NAME_UNEXPECTED_UNKNOWN_COMPONENT)
  private Float unexpectedUnknownComponent;

  public DirectiveNodeComplianceComplianceDetails() {
  }

  public DirectiveNodeComplianceComplianceDetails error(Float error) {
    this.error = error;
    return this;
  }

  /**
   * Get error
   * @return error
   */
  @javax.annotation.Nullable
  public Float getError() {
    return error;
  }

  public void setError(Float error) {
    this.error = error;
  }


  public DirectiveNodeComplianceComplianceDetails noReport(Float noReport) {
    this.noReport = noReport;
    return this;
  }

  /**
   * Get noReport
   * @return noReport
   */
  @javax.annotation.Nullable
  public Float getNoReport() {
    return noReport;
  }

  public void setNoReport(Float noReport) {
    this.noReport = noReport;
  }


  public DirectiveNodeComplianceComplianceDetails successAlreadyOK(Float successAlreadyOK) {
    this.successAlreadyOK = successAlreadyOK;
    return this;
  }

  /**
   * Get successAlreadyOK
   * @return successAlreadyOK
   */
  @javax.annotation.Nullable
  public Float getSuccessAlreadyOK() {
    return successAlreadyOK;
  }

  public void setSuccessAlreadyOK(Float successAlreadyOK) {
    this.successAlreadyOK = successAlreadyOK;
  }


  public DirectiveNodeComplianceComplianceDetails successNotApplicable(Float successNotApplicable) {
    this.successNotApplicable = successNotApplicable;
    return this;
  }

  /**
   * Get successNotApplicable
   * @return successNotApplicable
   */
  @javax.annotation.Nullable
  public Float getSuccessNotApplicable() {
    return successNotApplicable;
  }

  public void setSuccessNotApplicable(Float successNotApplicable) {
    this.successNotApplicable = successNotApplicable;
  }


  public DirectiveNodeComplianceComplianceDetails successRepaired(Float successRepaired) {
    this.successRepaired = successRepaired;
    return this;
  }

  /**
   * Get successRepaired
   * @return successRepaired
   */
  @javax.annotation.Nullable
  public Float getSuccessRepaired() {
    return successRepaired;
  }

  public void setSuccessRepaired(Float successRepaired) {
    this.successRepaired = successRepaired;
  }


  public DirectiveNodeComplianceComplianceDetails unexpectedMissingComponent(Float unexpectedMissingComponent) {
    this.unexpectedMissingComponent = unexpectedMissingComponent;
    return this;
  }

  /**
   * Get unexpectedMissingComponent
   * @return unexpectedMissingComponent
   */
  @javax.annotation.Nullable
  public Float getUnexpectedMissingComponent() {
    return unexpectedMissingComponent;
  }

  public void setUnexpectedMissingComponent(Float unexpectedMissingComponent) {
    this.unexpectedMissingComponent = unexpectedMissingComponent;
  }


  public DirectiveNodeComplianceComplianceDetails unexpectedUnknownComponent(Float unexpectedUnknownComponent) {
    this.unexpectedUnknownComponent = unexpectedUnknownComponent;
    return this;
  }

  /**
   * Get unexpectedUnknownComponent
   * @return unexpectedUnknownComponent
   */
  @javax.annotation.Nullable
  public Float getUnexpectedUnknownComponent() {
    return unexpectedUnknownComponent;
  }

  public void setUnexpectedUnknownComponent(Float unexpectedUnknownComponent) {
    this.unexpectedUnknownComponent = unexpectedUnknownComponent;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DirectiveNodeComplianceComplianceDetails directiveNodeComplianceComplianceDetails = (DirectiveNodeComplianceComplianceDetails) o;
    return Objects.equals(this.error, directiveNodeComplianceComplianceDetails.error) &&
        Objects.equals(this.noReport, directiveNodeComplianceComplianceDetails.noReport) &&
        Objects.equals(this.successAlreadyOK, directiveNodeComplianceComplianceDetails.successAlreadyOK) &&
        Objects.equals(this.successNotApplicable, directiveNodeComplianceComplianceDetails.successNotApplicable) &&
        Objects.equals(this.successRepaired, directiveNodeComplianceComplianceDetails.successRepaired) &&
        Objects.equals(this.unexpectedMissingComponent, directiveNodeComplianceComplianceDetails.unexpectedMissingComponent) &&
        Objects.equals(this.unexpectedUnknownComponent, directiveNodeComplianceComplianceDetails.unexpectedUnknownComponent);
  }

  @Override
  public int hashCode() {
    return Objects.hash(error, noReport, successAlreadyOK, successNotApplicable, successRepaired, unexpectedMissingComponent, unexpectedUnknownComponent);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DirectiveNodeComplianceComplianceDetails {\n");
    sb.append("    error: ").append(toIndentedString(error)).append("\n");
    sb.append("    noReport: ").append(toIndentedString(noReport)).append("\n");
    sb.append("    successAlreadyOK: ").append(toIndentedString(successAlreadyOK)).append("\n");
    sb.append("    successNotApplicable: ").append(toIndentedString(successNotApplicable)).append("\n");
    sb.append("    successRepaired: ").append(toIndentedString(successRepaired)).append("\n");
    sb.append("    unexpectedMissingComponent: ").append(toIndentedString(unexpectedMissingComponent)).append("\n");
    sb.append("    unexpectedUnknownComponent: ").append(toIndentedString(unexpectedUnknownComponent)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("error");
    openapiFields.add("noReport");
    openapiFields.add("successAlreadyOK");
    openapiFields.add("successNotApplicable");
    openapiFields.add("successRepaired");
    openapiFields.add("unexpectedMissingComponent");
    openapiFields.add("unexpectedUnknownComponent");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DirectiveNodeComplianceComplianceDetails
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DirectiveNodeComplianceComplianceDetails.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DirectiveNodeComplianceComplianceDetails is not found in the empty JSON string", DirectiveNodeComplianceComplianceDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DirectiveNodeComplianceComplianceDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DirectiveNodeComplianceComplianceDetails` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DirectiveNodeComplianceComplianceDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DirectiveNodeComplianceComplianceDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DirectiveNodeComplianceComplianceDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DirectiveNodeComplianceComplianceDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<DirectiveNodeComplianceComplianceDetails>() {
           @Override
           public void write(JsonWriter out, DirectiveNodeComplianceComplianceDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DirectiveNodeComplianceComplianceDetails read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DirectiveNodeComplianceComplianceDetails given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DirectiveNodeComplianceComplianceDetails
   * @throws IOException if the JSON string is invalid with respect to DirectiveNodeComplianceComplianceDetails
   */
  public static DirectiveNodeComplianceComplianceDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DirectiveNodeComplianceComplianceDetails.class);
  }

  /**
   * Convert an instance of DirectiveNodeComplianceComplianceDetails to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

