/*
 * Enode API
 * Download [OpenAPI 3.0 Specification](/OpenAPI-Enode-v1.4.0.json)  Download [Postman Collection](/Postman-Enode-v1.4.0.json)  The Enode API is designed to make smart charging applications easy to develop. We provide an abstraction layer that reduces the complexity when extracting vehicle data and sending commands to vehicles from a variety of manufacturers.  The API has a RESTful architecture and utilizes OAuth2 authorization.  We are always available to handle any issues or just answer your questions. Feel free to reach out on post@enode.io   ## Registration for API access In order to use the API you will need a `client_id` and `client_secret`. Please contact us if you are interested in using our API in production, and we will provide these credentials.  # Authorization Vehicle / hardware access via the Enode API is granted to your application by the User in a standard OAuth `Authorization Code` flow.  > The authorization scheme documented here is the recommended approach for most situations. However, it is also possible to user other OAuth flows, non-confidential clients, and temporary users. Please feel free to contact us if you have any questions about your use-case or the integration of your existing infrastructure.  ### Preparation: Configure your OAuth client  Because Enode API implements the OAuth 2.0 spec completely and without modifications, you can avoid rolling your own OAuth client implementation and instead use a well-supported and battle-tested implementation. This is strongly recommended. Information on available OAuth clients for many languages is available [here](https://oauth.net/code/)  To configure your chosen OAuth client, you will need these details: - Your `client_id` - Your `client_secret` - Authorization URL: `https://link.test.enode.io/oauth2/auth` - Token URL: `https://link.test.enode.io/oauth2/token`  ```javascript // Node.js + openid-client example const enodeIssuer = await Issuer.discover('https://link.test.enode.io'); const client = new enodeIssuer.Client({   client_id: 'xyz',   client_secret: 'shhhhh',   redirect_uris: ['http://localhost:5000/callback'],   response_types: ['code'], }); ```   ### Preparation: Obtain a client access token via OAuth Client Credentials Grant Your OAuth client will have a method for using the `OAuth 2.0 Client Credentials Grant` to obtain an access token.  ```javascript // Node.js + openid-client example const clientAccessToken = await client.grant({grant_type: \"client_credentials\"}); ```  This access token belongs to your client and is used for administrative actions, such as the next step.  This token should be cached by your server and reused until it expires, at which point your server should request a new one.    ### Step 1. Generate an Enode Link session for your User and launch the OAuth flow  When your User indicates that they want to connect their hardware to your app, your server must call [Link User](#operation/postUsersUseridLink) to generate an Enode Link session for your User. The User ID can be any string that uniquely identifies the User, but it is recommended that you use the primary key by which you identify the User within your application.  Example Request: ``` POST /users/{userId}/link HTTP/1.1 Authorization: Bearer {access_token} {   \"forceLanguage\": \"nb-NO\",   \"vendor\": \"Tesla\", } ```  Example Response: ``` {     \"linkState\": \"ZjE2MzMxMGFiYmU4MzcxOTU1ZmRjMTU5NGU2ZmE4YTU3NjViMzIwY2YzNG\", } ```  The returned linkState must be stored by your server, attached to the session of the authenticated user for which it was generated.  Your OAuth client will provide a method to construct an authorization URL for your user. That method will require these details: - Redirect URI - The URI to which your user should be redirected when the Oauth flow completes - Scope - The OAuth scope(s) you wish to request access to (see list of valid values [here](#section/Authentication/AccessTokenBearer)) - State - The value of `linkState` from the request above  To launch the OAuth flow, send your user to the authorization URL constructed by your OAuth client. This can be done in an embedded webview within a native iOS/Android app, or in the system's default browser.  ```javascript // Node.js + openid-client + express example  // Construct an OAuth authorization URL const authorizationUrl = client.authorizationUrl({   scope: \"offline_access all\",   state: linkState });  // Redirect user to authorization URL res.redirect(authorizationUrl); ```   ### Step 2. User grants consent In the Link UI webapp the user will follow 3 steps:  1. Choose their hardware from a list of supported manufacturers (EVs and charging boxes). For certain EV makes it will be necessary to also select a charge box. 2. For each selection, the user will be presented with the login screen for that particular hardware. The user must successfully log in. 3. A summary of the requested scopes will be presented to the user. The user must choose whether to grant access to your application.   ### Step 3. OAuth flow concludes with a callback When the user has completed their interactions, they will be redirected to the `Redirect URI` you provided in Step 1, with various metadata appended as query parameters.  Your OAuth client will have a method to parse and validate that metadata, and fetch the granted access and refresh tokens.  Among that metadata will be a `state` value - you must verify that it is equal to the `linkState` value persisted in Step 1, as [a countermeasure against CSRF attacks](https://tools.ietf.org/html/rfc6819#section-4.4.1.8).  ```javascript // Node.js + openid-client + express example  // Fetch linkState from user session const linkState = get(req, 'session.linkState');  // Parse relevant parameters from request URL const params = client.callbackParams(req);  // Exchange authorization code for access and refresh tokens // In this example, openid-client does the linkState validation check for us const tokenSet = await client.oauthCallback('http://localhost:5000/callback', params, {state: linkState}) ```  With the access token in hand, you can now access resources on behalf of the user.   # Errors And Problems ## OAuth Authorization Request  When the User has completed the process of allowing/denying access in Enode Link, they will be redirected to your configured redirect URI. If something has gone wrong, query parameters `error` and `error_description` will be set as documented in [Section 4.1.2.1](https://tools.ietf.org/html/rfc6749#section-4.1.2.1) of the OAuth 2.0 spec:  |error                      |error_description| |---------------------------|-----------------| |invalid_request            |The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed.| |unauthorized_client        |The client is not authorized to request an authorization code using this method.| |access_denied              |The resource owner or authorization server denied the request.| |unsupported_response_type  |The authorization server does not support obtaining an authorization code using this method.| |invalid_scope              |The requested scope is invalid, unknown, or malformed.| |server_error               |The authorization server encountered an unexpected condition that prevented it from fulfilling the request.| |temporarily_unavailable    |The authorization server is currently unable to handle the request due to a temporary overloading or maintenance of the server|  Example: ``` https://website.example/oauth_callback?state=e0a86fe5&error=access_denied&error_description=The+resource+owner+or+authorization+server+denied+the+request. ```   ## Errors when accessing a User's resources  When using an `access_token` to access a User's resources, the following HTTP Status Codes in the 4XX range may be encountered:  |HTTP Status Code           |Explanation      | |---------------------------|-----------------| |400 Bad Request            |The request payload has failed schema validation / parsing |401 Unauthorized           |Authentication details are missing or invalid |403 Forbidden              |Authentication succeeded, but the authenticated user doesn't have access to the resource |404 Not Found              |A non-existent resource is requested |429 Too Many Requests      |Rate limiting by the vendor has prevented us from completing the request   In all cases, an [RFC7807 Problem Details](https://tools.ietf.org/html/rfc7807) body is returned to aid in debugging.  Example: ``` HTTP/1.1 400 Bad Request Content-Type: application/problem+json {   \"type\": \"https://docs.enode.io/problems/payload-validation-error\",   \"title\": \"Payload validation failed\",   \"detail\": \"\\\"authorizationRequest.scope\\\" is required\", } ```  
 *
 * The version of the OpenAPI document: 1.3.10
 * 
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
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
 * GetVehicleChargestate200Response
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:22:00.443378-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class GetVehicleChargestate200Response {
  public static final String SERIALIZED_NAME_BATTERY_CAPACITY = "batteryCapacity";
  @SerializedName(SERIALIZED_NAME_BATTERY_CAPACITY)
  private BigDecimal batteryCapacity;

  public static final String SERIALIZED_NAME_BATTERY_LEVEL = "batteryLevel";
  @SerializedName(SERIALIZED_NAME_BATTERY_LEVEL)
  private BigDecimal batteryLevel;

  public static final String SERIALIZED_NAME_CHARGE_LIMIT = "chargeLimit";
  @SerializedName(SERIALIZED_NAME_CHARGE_LIMIT)
  private BigDecimal chargeLimit;

  public static final String SERIALIZED_NAME_CHARGE_RATE = "chargeRate";
  @SerializedName(SERIALIZED_NAME_CHARGE_RATE)
  private BigDecimal chargeRate;

  public static final String SERIALIZED_NAME_CHARGE_TIME_REMAINING = "chargeTimeRemaining";
  @SerializedName(SERIALIZED_NAME_CHARGE_TIME_REMAINING)
  private BigDecimal chargeTimeRemaining;

  public static final String SERIALIZED_NAME_IS_CHARGING = "isCharging";
  @SerializedName(SERIALIZED_NAME_IS_CHARGING)
  private Boolean isCharging;

  /**
   * Gets or Sets isChargingReasons
   */
  @JsonAdapter(IsChargingReasonsEnum.Adapter.class)
  public enum IsChargingReasonsEnum {
    _OVERRIDE_TRUE_("{\"override\":true}"),
    
    DEFAULT("DEFAULT");

    private String value;

    IsChargingReasonsEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static IsChargingReasonsEnum fromValue(String value) {
      for (IsChargingReasonsEnum b : IsChargingReasonsEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<IsChargingReasonsEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final IsChargingReasonsEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public IsChargingReasonsEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return IsChargingReasonsEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      IsChargingReasonsEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_IS_CHARGING_REASONS = "isChargingReasons";
  @SerializedName(SERIALIZED_NAME_IS_CHARGING_REASONS)
  private List<IsChargingReasonsEnum> isChargingReasons = new ArrayList<>();

  public static final String SERIALIZED_NAME_IS_PLUGGED_IN = "isPluggedIn";
  @SerializedName(SERIALIZED_NAME_IS_PLUGGED_IN)
  private Boolean isPluggedIn;

  public static final String SERIALIZED_NAME_RANGE = "range";
  @SerializedName(SERIALIZED_NAME_RANGE)
  private BigDecimal range;

  public GetVehicleChargestate200Response() {
  }

  public GetVehicleChargestate200Response batteryCapacity(BigDecimal batteryCapacity) {
    this.batteryCapacity = batteryCapacity;
    return this;
  }

  /**
   * Vehicle&#39;s maximum physical battery capacity in kWh. This number slowly decreases/degrades over time.
   * minimum: 0
   * @return batteryCapacity
   */
  @javax.annotation.Nullable
  public BigDecimal getBatteryCapacity() {
    return batteryCapacity;
  }

  public void setBatteryCapacity(BigDecimal batteryCapacity) {
    this.batteryCapacity = batteryCapacity;
  }


  public GetVehicleChargestate200Response batteryLevel(BigDecimal batteryLevel) {
    this.batteryLevel = batteryLevel;
    return this;
  }

  /**
   * Remaining battery in percent
   * minimum: 0
   * maximum: 100
   * @return batteryLevel
   */
  @javax.annotation.Nullable
  public BigDecimal getBatteryLevel() {
    return batteryLevel;
  }

  public void setBatteryLevel(BigDecimal batteryLevel) {
    this.batteryLevel = batteryLevel;
  }


  public GetVehicleChargestate200Response chargeLimit(BigDecimal chargeLimit) {
    this.chargeLimit = chargeLimit;
    return this;
  }

  /**
   * Charge limit, as a percent of &#x60;batteryCapacity&#x60;.
   * minimum: 0
   * maximum: 100
   * @return chargeLimit
   */
  @javax.annotation.Nullable
  public BigDecimal getChargeLimit() {
    return chargeLimit;
  }

  public void setChargeLimit(BigDecimal chargeLimit) {
    this.chargeLimit = chargeLimit;
  }


  public GetVehicleChargestate200Response chargeRate(BigDecimal chargeRate) {
    this.chargeRate = chargeRate;
    return this;
  }

  /**
   * The current charge rate in kW.  This property is only available when the vehicle is charging, and is &#x60;null&#x60; any other time.
   * minimum: 0
   * @return chargeRate
   */
  @javax.annotation.Nullable
  public BigDecimal getChargeRate() {
    return chargeRate;
  }

  public void setChargeRate(BigDecimal chargeRate) {
    this.chargeRate = chargeRate;
  }


  public GetVehicleChargestate200Response chargeTimeRemaining(BigDecimal chargeTimeRemaining) {
    this.chargeTimeRemaining = chargeTimeRemaining;
    return this;
  }

  /**
   * Estimated time until the current charging intent is completed, in minutes.  This property is only available when the vehicle is charging, and is &#x60;null&#x60; any other time.
   * @return chargeTimeRemaining
   */
  @javax.annotation.Nullable
  public BigDecimal getChargeTimeRemaining() {
    return chargeTimeRemaining;
  }

  public void setChargeTimeRemaining(BigDecimal chargeTimeRemaining) {
    this.chargeTimeRemaining = chargeTimeRemaining;
  }


  public GetVehicleChargestate200Response isCharging(Boolean isCharging) {
    this.isCharging = isCharging;
    return this;
  }

  /**
   * Current charging status of the vehicle
   * @return isCharging
   */
  @javax.annotation.Nullable
  public Boolean getIsCharging() {
    return isCharging;
  }

  public void setIsCharging(Boolean isCharging) {
    this.isCharging = isCharging;
  }


  public GetVehicleChargestate200Response isChargingReasons(List<IsChargingReasonsEnum> isChargingReasons) {
    this.isChargingReasons = isChargingReasons;
    return this;
  }

  public GetVehicleChargestate200Response addIsChargingReasonsItem(IsChargingReasonsEnum isChargingReasonsItem) {
    if (this.isChargingReasons == null) {
      this.isChargingReasons = new ArrayList<>();
    }
    this.isChargingReasons.add(isChargingReasonsItem);
    return this;
  }

  /**
   * Array of string constants that explain why the car is or is not charging. May contain multiple values.  **Any:** - DEFAULT - the car is not being controlled by Enode  **Not Charging:** - NOT_PLUGGED_IN - because the car is not plugged into a charger - FULLY_CHARGED - because the car is fully charged - MANUALLY_STOPPED - because the car has been manually commanded to stop charging - SMART_CHARGING_DELAY - because Smart Charging has identified an opportunity to delay charging until prices are lower  **Charging:** - MANUALLY_STARTED - because the car has been manually commanded to start charging - SMART_CHARGING_ACTIVE - because Smart Charging has identified that this is an optimal time to charge - SMART_CHARGING_DEADLINE - because, regardless of price, charging must be active to meet the configured deadline
   * @return isChargingReasons
   */
  @javax.annotation.Nullable
  public List<IsChargingReasonsEnum> getIsChargingReasons() {
    return isChargingReasons;
  }

  public void setIsChargingReasons(List<IsChargingReasonsEnum> isChargingReasons) {
    this.isChargingReasons = isChargingReasons;
  }


  public GetVehicleChargestate200Response isPluggedIn(Boolean isPluggedIn) {
    this.isPluggedIn = isPluggedIn;
    return this;
  }

  /**
   * Indicates whether the vehicle is connected to a charging box (regardless of whether it is actually charging)
   * @return isPluggedIn
   */
  @javax.annotation.Nullable
  public Boolean getIsPluggedIn() {
    return isPluggedIn;
  }

  public void setIsPluggedIn(Boolean isPluggedIn) {
    this.isPluggedIn = isPluggedIn;
  }


  public GetVehicleChargestate200Response range(BigDecimal range) {
    this.range = range;
    return this;
  }

  /**
   * Estimated remaining kilometers
   * minimum: 0
   * @return range
   */
  @javax.annotation.Nullable
  public BigDecimal getRange() {
    return range;
  }

  public void setRange(BigDecimal range) {
    this.range = range;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetVehicleChargestate200Response getVehicleChargestate200Response = (GetVehicleChargestate200Response) o;
    return Objects.equals(this.batteryCapacity, getVehicleChargestate200Response.batteryCapacity) &&
        Objects.equals(this.batteryLevel, getVehicleChargestate200Response.batteryLevel) &&
        Objects.equals(this.chargeLimit, getVehicleChargestate200Response.chargeLimit) &&
        Objects.equals(this.chargeRate, getVehicleChargestate200Response.chargeRate) &&
        Objects.equals(this.chargeTimeRemaining, getVehicleChargestate200Response.chargeTimeRemaining) &&
        Objects.equals(this.isCharging, getVehicleChargestate200Response.isCharging) &&
        Objects.equals(this.isChargingReasons, getVehicleChargestate200Response.isChargingReasons) &&
        Objects.equals(this.isPluggedIn, getVehicleChargestate200Response.isPluggedIn) &&
        Objects.equals(this.range, getVehicleChargestate200Response.range);
  }

  @Override
  public int hashCode() {
    return Objects.hash(batteryCapacity, batteryLevel, chargeLimit, chargeRate, chargeTimeRemaining, isCharging, isChargingReasons, isPluggedIn, range);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetVehicleChargestate200Response {\n");
    sb.append("    batteryCapacity: ").append(toIndentedString(batteryCapacity)).append("\n");
    sb.append("    batteryLevel: ").append(toIndentedString(batteryLevel)).append("\n");
    sb.append("    chargeLimit: ").append(toIndentedString(chargeLimit)).append("\n");
    sb.append("    chargeRate: ").append(toIndentedString(chargeRate)).append("\n");
    sb.append("    chargeTimeRemaining: ").append(toIndentedString(chargeTimeRemaining)).append("\n");
    sb.append("    isCharging: ").append(toIndentedString(isCharging)).append("\n");
    sb.append("    isChargingReasons: ").append(toIndentedString(isChargingReasons)).append("\n");
    sb.append("    isPluggedIn: ").append(toIndentedString(isPluggedIn)).append("\n");
    sb.append("    range: ").append(toIndentedString(range)).append("\n");
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
    openapiFields.add("batteryCapacity");
    openapiFields.add("batteryLevel");
    openapiFields.add("chargeLimit");
    openapiFields.add("chargeRate");
    openapiFields.add("chargeTimeRemaining");
    openapiFields.add("isCharging");
    openapiFields.add("isChargingReasons");
    openapiFields.add("isPluggedIn");
    openapiFields.add("range");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to GetVehicleChargestate200Response
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!GetVehicleChargestate200Response.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in GetVehicleChargestate200Response is not found in the empty JSON string", GetVehicleChargestate200Response.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!GetVehicleChargestate200Response.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `GetVehicleChargestate200Response` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("isChargingReasons") != null && !jsonObj.get("isChargingReasons").isJsonNull() && !jsonObj.get("isChargingReasons").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `isChargingReasons` to be an array in the JSON string but got `%s`", jsonObj.get("isChargingReasons").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!GetVehicleChargestate200Response.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'GetVehicleChargestate200Response' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<GetVehicleChargestate200Response> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(GetVehicleChargestate200Response.class));

       return (TypeAdapter<T>) new TypeAdapter<GetVehicleChargestate200Response>() {
           @Override
           public void write(JsonWriter out, GetVehicleChargestate200Response value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public GetVehicleChargestate200Response read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of GetVehicleChargestate200Response given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of GetVehicleChargestate200Response
   * @throws IOException if the JSON string is invalid with respect to GetVehicleChargestate200Response
   */
  public static GetVehicleChargestate200Response fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, GetVehicleChargestate200Response.class);
  }

  /**
   * Convert an instance of GetVehicleChargestate200Response to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

