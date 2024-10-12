/*
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
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
 * ThreeDSecureResult
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ThreeDSecureResult {
  /**
   * 3D Secure authentication response status.
   */
  @JsonAdapter(AuthenticatedEnum.Adapter.class)
  public enum AuthenticatedEnum {
    TRUE("true"),
    
    FALSE("false"),
    
    NOT_APPLICABLE("not applicable"),
    
    ATTEMPTED("attempted");

    private String value;

    AuthenticatedEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AuthenticatedEnum fromValue(String value) {
      for (AuthenticatedEnum b : AuthenticatedEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AuthenticatedEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AuthenticatedEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AuthenticatedEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AuthenticatedEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AuthenticatedEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_AUTHENTICATED = "authenticated";
  @SerializedName(SERIALIZED_NAME_AUTHENTICATED)
  private AuthenticatedEnum authenticated;

  /**
   * Is the cardholder enrolled in 3D Secure.
   */
  @JsonAdapter(EnrolledEnum.Adapter.class)
  public enum EnrolledEnum {
    TRUE("true"),
    
    FALSE("false"),
    
    INVALID_CARD_TIMEOUT("invalid card/timeout"),
    
    UNAVAILABLE("unavailable");

    private String value;

    EnrolledEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static EnrolledEnum fromValue(String value) {
      for (EnrolledEnum b : EnrolledEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<EnrolledEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final EnrolledEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public EnrolledEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return EnrolledEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      EnrolledEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ENROLLED = "enrolled";
  @SerializedName(SERIALIZED_NAME_ENROLLED)
  private EnrolledEnum enrolled;

  /**
   * 3D Secure 2 authentication flow.
   */
  @JsonAdapter(FlowEnum.Adapter.class)
  public enum FlowEnum {
    FRICTIONLESS("frictionless"),
    
    CHALLENGE("challenge");

    private String value;

    FlowEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static FlowEnum fromValue(String value) {
      for (FlowEnum b : FlowEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<FlowEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final FlowEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public FlowEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return FlowEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      FlowEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_FLOW = "flow";
  @SerializedName(SERIALIZED_NAME_FLOW)
  private FlowEnum flow;

  public static final String SERIALIZED_NAME_IS_DOWNGRADED = "isDowngraded";
  @SerializedName(SERIALIZED_NAME_IS_DOWNGRADED)
  private Boolean isDowngraded = false;

  /**
   * Gets or Sets liability
   */
  @JsonAdapter(LiabilityEnum.Adapter.class)
  public enum LiabilityEnum {
    PROTECTED("protected"),
    
    NOT_PROTECTED("not protected"),
    
    PROTECTED_ATTEMPT_("protected (attempt)");

    private String value;

    LiabilityEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static LiabilityEnum fromValue(String value) {
      for (LiabilityEnum b : LiabilityEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<LiabilityEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final LiabilityEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public LiabilityEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return LiabilityEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      LiabilityEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_LIABILITY = "liability";
  @SerializedName(SERIALIZED_NAME_LIABILITY)
  private LiabilityEnum liability;

  /**
   * 3D Secure version.
   */
  @JsonAdapter(VersionEnum.Adapter.class)
  public enum VersionEnum {
    _1_0_2("1.0.2"),
    
    _2_1_0("2.1.0"),
    
    _2_2_0("2.2.0");

    private String value;

    VersionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static VersionEnum fromValue(String value) {
      for (VersionEnum b : VersionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<VersionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final VersionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public VersionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return VersionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      VersionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_VERSION = "version";
  @SerializedName(SERIALIZED_NAME_VERSION)
  private VersionEnum version;

  public ThreeDSecureResult() {
  }

  public ThreeDSecureResult authenticated(AuthenticatedEnum authenticated) {
    this.authenticated = authenticated;
    return this;
  }

  /**
   * 3D Secure authentication response status.
   * @return authenticated
   */
  @javax.annotation.Nonnull
  public AuthenticatedEnum getAuthenticated() {
    return authenticated;
  }

  public void setAuthenticated(AuthenticatedEnum authenticated) {
    this.authenticated = authenticated;
  }


  public ThreeDSecureResult enrolled(EnrolledEnum enrolled) {
    this.enrolled = enrolled;
    return this;
  }

  /**
   * Is the cardholder enrolled in 3D Secure.
   * @return enrolled
   */
  @javax.annotation.Nonnull
  public EnrolledEnum getEnrolled() {
    return enrolled;
  }

  public void setEnrolled(EnrolledEnum enrolled) {
    this.enrolled = enrolled;
  }


  public ThreeDSecureResult flow(FlowEnum flow) {
    this.flow = flow;
    return this;
  }

  /**
   * 3D Secure 2 authentication flow.
   * @return flow
   */
  @javax.annotation.Nullable
  public FlowEnum getFlow() {
    return flow;
  }

  public void setFlow(FlowEnum flow) {
    this.flow = flow;
  }


  public ThreeDSecureResult isDowngraded(Boolean isDowngraded) {
    this.isDowngraded = isDowngraded;
    return this;
  }

  /**
   * If 3D Secure 2 was attempted but downgraded to 3D Secure 1.
   * @return isDowngraded
   */
  @javax.annotation.Nonnull
  public Boolean getIsDowngraded() {
    return isDowngraded;
  }

  public void setIsDowngraded(Boolean isDowngraded) {
    this.isDowngraded = isDowngraded;
  }


  public ThreeDSecureResult liability(LiabilityEnum liability) {
    this.liability = liability;
    return this;
  }

  /**
   * Get liability
   * @return liability
   */
  @javax.annotation.Nonnull
  public LiabilityEnum getLiability() {
    return liability;
  }

  public void setLiability(LiabilityEnum liability) {
    this.liability = liability;
  }


  public ThreeDSecureResult version(VersionEnum version) {
    this.version = version;
    return this;
  }

  /**
   * 3D Secure version.
   * @return version
   */
  @javax.annotation.Nullable
  public VersionEnum getVersion() {
    return version;
  }

  public void setVersion(VersionEnum version) {
    this.version = version;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ThreeDSecureResult threeDSecureResult = (ThreeDSecureResult) o;
    return Objects.equals(this.authenticated, threeDSecureResult.authenticated) &&
        Objects.equals(this.enrolled, threeDSecureResult.enrolled) &&
        Objects.equals(this.flow, threeDSecureResult.flow) &&
        Objects.equals(this.isDowngraded, threeDSecureResult.isDowngraded) &&
        Objects.equals(this.liability, threeDSecureResult.liability) &&
        Objects.equals(this.version, threeDSecureResult.version);
  }

  @Override
  public int hashCode() {
    return Objects.hash(authenticated, enrolled, flow, isDowngraded, liability, version);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ThreeDSecureResult {\n");
    sb.append("    authenticated: ").append(toIndentedString(authenticated)).append("\n");
    sb.append("    enrolled: ").append(toIndentedString(enrolled)).append("\n");
    sb.append("    flow: ").append(toIndentedString(flow)).append("\n");
    sb.append("    isDowngraded: ").append(toIndentedString(isDowngraded)).append("\n");
    sb.append("    liability: ").append(toIndentedString(liability)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
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
    openapiFields.add("authenticated");
    openapiFields.add("enrolled");
    openapiFields.add("flow");
    openapiFields.add("isDowngraded");
    openapiFields.add("liability");
    openapiFields.add("version");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("authenticated");
    openapiRequiredFields.add("enrolled");
    openapiRequiredFields.add("isDowngraded");
    openapiRequiredFields.add("liability");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ThreeDSecureResult
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ThreeDSecureResult.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ThreeDSecureResult is not found in the empty JSON string", ThreeDSecureResult.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ThreeDSecureResult.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ThreeDSecureResult` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ThreeDSecureResult.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("authenticated").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `authenticated` to be a primitive type in the JSON string but got `%s`", jsonObj.get("authenticated").toString()));
      }
      // validate the required field `authenticated`
      AuthenticatedEnum.validateJsonElement(jsonObj.get("authenticated"));
      if (!jsonObj.get("enrolled").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `enrolled` to be a primitive type in the JSON string but got `%s`", jsonObj.get("enrolled").toString()));
      }
      // validate the required field `enrolled`
      EnrolledEnum.validateJsonElement(jsonObj.get("enrolled"));
      if ((jsonObj.get("flow") != null && !jsonObj.get("flow").isJsonNull()) && !jsonObj.get("flow").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `flow` to be a primitive type in the JSON string but got `%s`", jsonObj.get("flow").toString()));
      }
      // validate the optional field `flow`
      if (jsonObj.get("flow") != null && !jsonObj.get("flow").isJsonNull()) {
        FlowEnum.validateJsonElement(jsonObj.get("flow"));
      }
      if (!jsonObj.get("liability").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `liability` to be a primitive type in the JSON string but got `%s`", jsonObj.get("liability").toString()));
      }
      // validate the required field `liability`
      LiabilityEnum.validateJsonElement(jsonObj.get("liability"));
      if ((jsonObj.get("version") != null && !jsonObj.get("version").isJsonNull()) && !jsonObj.get("version").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `version` to be a primitive type in the JSON string but got `%s`", jsonObj.get("version").toString()));
      }
      // validate the optional field `version`
      if (jsonObj.get("version") != null && !jsonObj.get("version").isJsonNull()) {
        VersionEnum.validateJsonElement(jsonObj.get("version"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ThreeDSecureResult.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ThreeDSecureResult' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ThreeDSecureResult> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ThreeDSecureResult.class));

       return (TypeAdapter<T>) new TypeAdapter<ThreeDSecureResult>() {
           @Override
           public void write(JsonWriter out, ThreeDSecureResult value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ThreeDSecureResult read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ThreeDSecureResult given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ThreeDSecureResult
   * @throws IOException if the JSON string is invalid with respect to ThreeDSecureResult
   */
  public static ThreeDSecureResult fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ThreeDSecureResult.class);
  }

  /**
   * Convert an instance of ThreeDSecureResult to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

