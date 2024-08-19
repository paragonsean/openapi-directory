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
import org.openapitools.client.model.Color;
import org.openapitools.client.model.Logo;

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
 * BrandingConf
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:58.781092-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BrandingConf {
  public static final String SERIALIZED_NAME_BAR_COLOR = "barColor";
  @SerializedName(SERIALIZED_NAME_BAR_COLOR)
  private Color barColor;

  public static final String SERIALIZED_NAME_DISPLAY_BAR = "displayBar";
  @SerializedName(SERIALIZED_NAME_DISPLAY_BAR)
  private Boolean displayBar;

  public static final String SERIALIZED_NAME_DISPLAY_BAR_LOGIN = "displayBarLogin";
  @SerializedName(SERIALIZED_NAME_DISPLAY_BAR_LOGIN)
  private Boolean displayBarLogin;

  public static final String SERIALIZED_NAME_DISPLAY_LABEL = "displayLabel";
  @SerializedName(SERIALIZED_NAME_DISPLAY_LABEL)
  private Boolean displayLabel;

  public static final String SERIALIZED_NAME_DISPLAY_MOTD = "displayMotd";
  @SerializedName(SERIALIZED_NAME_DISPLAY_MOTD)
  private Boolean displayMotd;

  public static final String SERIALIZED_NAME_LABEL_COLOR = "labelColor";
  @SerializedName(SERIALIZED_NAME_LABEL_COLOR)
  private Color labelColor;

  public static final String SERIALIZED_NAME_LABEL_TEXT = "labelText";
  @SerializedName(SERIALIZED_NAME_LABEL_TEXT)
  private String labelText;

  public static final String SERIALIZED_NAME_MOTD = "motd";
  @SerializedName(SERIALIZED_NAME_MOTD)
  private String motd;

  public static final String SERIALIZED_NAME_SMALL_LOGO = "smallLogo";
  @SerializedName(SERIALIZED_NAME_SMALL_LOGO)
  private Logo smallLogo;

  public static final String SERIALIZED_NAME_WIDE_LOGO = "wideLogo";
  @SerializedName(SERIALIZED_NAME_WIDE_LOGO)
  private Logo wideLogo;

  public BrandingConf() {
  }

  public BrandingConf barColor(Color barColor) {
    this.barColor = barColor;
    return this;
  }

  /**
   * Get barColor
   * @return barColor
   */
  @javax.annotation.Nonnull
  public Color getBarColor() {
    return barColor;
  }

  public void setBarColor(Color barColor) {
    this.barColor = barColor;
  }


  public BrandingConf displayBar(Boolean displayBar) {
    this.displayBar = displayBar;
    return this;
  }

  /**
   * Whether header bar is displayed or not
   * @return displayBar
   */
  @javax.annotation.Nonnull
  public Boolean getDisplayBar() {
    return displayBar;
  }

  public void setDisplayBar(Boolean displayBar) {
    this.displayBar = displayBar;
  }


  public BrandingConf displayBarLogin(Boolean displayBarLogin) {
    this.displayBarLogin = displayBarLogin;
    return this;
  }

  /**
   * Whether header bar is displayed in login page or not
   * @return displayBarLogin
   */
  @javax.annotation.Nonnull
  public Boolean getDisplayBarLogin() {
    return displayBarLogin;
  }

  public void setDisplayBarLogin(Boolean displayBarLogin) {
    this.displayBarLogin = displayBarLogin;
  }


  public BrandingConf displayLabel(Boolean displayLabel) {
    this.displayLabel = displayLabel;
    return this;
  }

  /**
   * Whether header bar&#39;s label is displayed or not
   * @return displayLabel
   */
  @javax.annotation.Nonnull
  public Boolean getDisplayLabel() {
    return displayLabel;
  }

  public void setDisplayLabel(Boolean displayLabel) {
    this.displayLabel = displayLabel;
  }


  public BrandingConf displayMotd(Boolean displayMotd) {
    this.displayMotd = displayMotd;
    return this;
  }

  /**
   * Whether the message of the day is displayed in login page or not
   * @return displayMotd
   */
  @javax.annotation.Nonnull
  public Boolean getDisplayMotd() {
    return displayMotd;
  }

  public void setDisplayMotd(Boolean displayMotd) {
    this.displayMotd = displayMotd;
  }


  public BrandingConf labelColor(Color labelColor) {
    this.labelColor = labelColor;
    return this;
  }

  /**
   * Get labelColor
   * @return labelColor
   */
  @javax.annotation.Nonnull
  public Color getLabelColor() {
    return labelColor;
  }

  public void setLabelColor(Color labelColor) {
    this.labelColor = labelColor;
  }


  public BrandingConf labelText(String labelText) {
    this.labelText = labelText;
    return this;
  }

  /**
   * The header bar&#39;s label title
   * @return labelText
   */
  @javax.annotation.Nonnull
  public String getLabelText() {
    return labelText;
  }

  public void setLabelText(String labelText) {
    this.labelText = labelText;
  }


  public BrandingConf motd(String motd) {
    this.motd = motd;
    return this;
  }

  /**
   * Message of the day in login page
   * @return motd
   */
  @javax.annotation.Nonnull
  public String getMotd() {
    return motd;
  }

  public void setMotd(String motd) {
    this.motd = motd;
  }


  public BrandingConf smallLogo(Logo smallLogo) {
    this.smallLogo = smallLogo;
    return this;
  }

  /**
   * Get smallLogo
   * @return smallLogo
   */
  @javax.annotation.Nonnull
  public Logo getSmallLogo() {
    return smallLogo;
  }

  public void setSmallLogo(Logo smallLogo) {
    this.smallLogo = smallLogo;
  }


  public BrandingConf wideLogo(Logo wideLogo) {
    this.wideLogo = wideLogo;
    return this;
  }

  /**
   * Get wideLogo
   * @return wideLogo
   */
  @javax.annotation.Nonnull
  public Logo getWideLogo() {
    return wideLogo;
  }

  public void setWideLogo(Logo wideLogo) {
    this.wideLogo = wideLogo;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BrandingConf brandingConf = (BrandingConf) o;
    return Objects.equals(this.barColor, brandingConf.barColor) &&
        Objects.equals(this.displayBar, brandingConf.displayBar) &&
        Objects.equals(this.displayBarLogin, brandingConf.displayBarLogin) &&
        Objects.equals(this.displayLabel, brandingConf.displayLabel) &&
        Objects.equals(this.displayMotd, brandingConf.displayMotd) &&
        Objects.equals(this.labelColor, brandingConf.labelColor) &&
        Objects.equals(this.labelText, brandingConf.labelText) &&
        Objects.equals(this.motd, brandingConf.motd) &&
        Objects.equals(this.smallLogo, brandingConf.smallLogo) &&
        Objects.equals(this.wideLogo, brandingConf.wideLogo);
  }

  @Override
  public int hashCode() {
    return Objects.hash(barColor, displayBar, displayBarLogin, displayLabel, displayMotd, labelColor, labelText, motd, smallLogo, wideLogo);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BrandingConf {\n");
    sb.append("    barColor: ").append(toIndentedString(barColor)).append("\n");
    sb.append("    displayBar: ").append(toIndentedString(displayBar)).append("\n");
    sb.append("    displayBarLogin: ").append(toIndentedString(displayBarLogin)).append("\n");
    sb.append("    displayLabel: ").append(toIndentedString(displayLabel)).append("\n");
    sb.append("    displayMotd: ").append(toIndentedString(displayMotd)).append("\n");
    sb.append("    labelColor: ").append(toIndentedString(labelColor)).append("\n");
    sb.append("    labelText: ").append(toIndentedString(labelText)).append("\n");
    sb.append("    motd: ").append(toIndentedString(motd)).append("\n");
    sb.append("    smallLogo: ").append(toIndentedString(smallLogo)).append("\n");
    sb.append("    wideLogo: ").append(toIndentedString(wideLogo)).append("\n");
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
    openapiFields.add("barColor");
    openapiFields.add("displayBar");
    openapiFields.add("displayBarLogin");
    openapiFields.add("displayLabel");
    openapiFields.add("displayMotd");
    openapiFields.add("labelColor");
    openapiFields.add("labelText");
    openapiFields.add("motd");
    openapiFields.add("smallLogo");
    openapiFields.add("wideLogo");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("barColor");
    openapiRequiredFields.add("displayBar");
    openapiRequiredFields.add("displayBarLogin");
    openapiRequiredFields.add("displayLabel");
    openapiRequiredFields.add("displayMotd");
    openapiRequiredFields.add("labelColor");
    openapiRequiredFields.add("labelText");
    openapiRequiredFields.add("motd");
    openapiRequiredFields.add("smallLogo");
    openapiRequiredFields.add("wideLogo");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BrandingConf
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BrandingConf.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BrandingConf is not found in the empty JSON string", BrandingConf.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BrandingConf.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BrandingConf` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : BrandingConf.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `barColor`
      Color.validateJsonElement(jsonObj.get("barColor"));
      // validate the required field `labelColor`
      Color.validateJsonElement(jsonObj.get("labelColor"));
      if (!jsonObj.get("labelText").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `labelText` to be a primitive type in the JSON string but got `%s`", jsonObj.get("labelText").toString()));
      }
      if (!jsonObj.get("motd").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `motd` to be a primitive type in the JSON string but got `%s`", jsonObj.get("motd").toString()));
      }
      // validate the required field `smallLogo`
      Logo.validateJsonElement(jsonObj.get("smallLogo"));
      // validate the required field `wideLogo`
      Logo.validateJsonElement(jsonObj.get("wideLogo"));
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BrandingConf.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BrandingConf' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BrandingConf> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BrandingConf.class));

       return (TypeAdapter<T>) new TypeAdapter<BrandingConf>() {
           @Override
           public void write(JsonWriter out, BrandingConf value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BrandingConf read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BrandingConf given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BrandingConf
   * @throws IOException if the JSON string is invalid with respect to BrandingConf
   */
  public static BrandingConf fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BrandingConf.class);
  }

  /**
   * Convert an instance of BrandingConf to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

