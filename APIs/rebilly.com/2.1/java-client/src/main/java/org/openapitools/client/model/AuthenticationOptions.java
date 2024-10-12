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
 * AuthenticationOptions
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AuthenticationOptions {
  public static final String SERIALIZED_NAME_AUTH_TOKEN_TTL = "authTokenTtl";
  @SerializedName(SERIALIZED_NAME_AUTH_TOKEN_TTL)
  private Integer authTokenTtl;

  public static final String SERIALIZED_NAME_CREDENTIAL_TTL = "credentialTtl";
  @SerializedName(SERIALIZED_NAME_CREDENTIAL_TTL)
  private Integer credentialTtl;

  public static final String SERIALIZED_NAME_OTP_REQUIRED = "otpRequired";
  @SerializedName(SERIALIZED_NAME_OTP_REQUIRED)
  private Boolean otpRequired;

  public static final String SERIALIZED_NAME_PASSWORD_PATTERN = "passwordPattern";
  @SerializedName(SERIALIZED_NAME_PASSWORD_PATTERN)
  private String passwordPattern;

  public static final String SERIALIZED_NAME_RESET_TOKEN_TTL = "resetTokenTtl";
  @SerializedName(SERIALIZED_NAME_RESET_TOKEN_TTL)
  private Integer resetTokenTtl;

  public AuthenticationOptions() {
  }

  public AuthenticationOptions authTokenTtl(Integer authTokenTtl) {
    this.authTokenTtl = authTokenTtl;
    return this;
  }

  /**
   * The default lifetime of the auth-token in seconds.
   * @return authTokenTtl
   */
  @javax.annotation.Nullable
  public Integer getAuthTokenTtl() {
    return authTokenTtl;
  }

  public void setAuthTokenTtl(Integer authTokenTtl) {
    this.authTokenTtl = authTokenTtl;
  }


  public AuthenticationOptions credentialTtl(Integer credentialTtl) {
    this.credentialTtl = credentialTtl;
    return this;
  }

  /**
   * The default lifetime of the credential in seconds.
   * @return credentialTtl
   */
  @javax.annotation.Nullable
  public Integer getCredentialTtl() {
    return credentialTtl;
  }

  public void setCredentialTtl(Integer credentialTtl) {
    this.credentialTtl = credentialTtl;
  }


  public AuthenticationOptions otpRequired(Boolean otpRequired) {
    this.otpRequired = otpRequired;
    return this;
  }

  /**
   * Should OTP be required to exchange token.
   * @return otpRequired
   */
  @javax.annotation.Nullable
  public Boolean getOtpRequired() {
    return otpRequired;
  }

  public void setOtpRequired(Boolean otpRequired) {
    this.otpRequired = otpRequired;
  }


  public AuthenticationOptions passwordPattern(String passwordPattern) {
    this.passwordPattern = passwordPattern;
    return this;
  }

  /**
   * Allowed password pattern.
   * @return passwordPattern
   */
  @javax.annotation.Nullable
  public String getPasswordPattern() {
    return passwordPattern;
  }

  public void setPasswordPattern(String passwordPattern) {
    this.passwordPattern = passwordPattern;
  }


  public AuthenticationOptions resetTokenTtl(Integer resetTokenTtl) {
    this.resetTokenTtl = resetTokenTtl;
    return this;
  }

  /**
   * The default lifetime of the reset-token in seconds.
   * @return resetTokenTtl
   */
  @javax.annotation.Nullable
  public Integer getResetTokenTtl() {
    return resetTokenTtl;
  }

  public void setResetTokenTtl(Integer resetTokenTtl) {
    this.resetTokenTtl = resetTokenTtl;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AuthenticationOptions authenticationOptions = (AuthenticationOptions) o;
    return Objects.equals(this.authTokenTtl, authenticationOptions.authTokenTtl) &&
        Objects.equals(this.credentialTtl, authenticationOptions.credentialTtl) &&
        Objects.equals(this.otpRequired, authenticationOptions.otpRequired) &&
        Objects.equals(this.passwordPattern, authenticationOptions.passwordPattern) &&
        Objects.equals(this.resetTokenTtl, authenticationOptions.resetTokenTtl);
  }

  @Override
  public int hashCode() {
    return Objects.hash(authTokenTtl, credentialTtl, otpRequired, passwordPattern, resetTokenTtl);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AuthenticationOptions {\n");
    sb.append("    authTokenTtl: ").append(toIndentedString(authTokenTtl)).append("\n");
    sb.append("    credentialTtl: ").append(toIndentedString(credentialTtl)).append("\n");
    sb.append("    otpRequired: ").append(toIndentedString(otpRequired)).append("\n");
    sb.append("    passwordPattern: ").append(toIndentedString(passwordPattern)).append("\n");
    sb.append("    resetTokenTtl: ").append(toIndentedString(resetTokenTtl)).append("\n");
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
    openapiFields.add("authTokenTtl");
    openapiFields.add("credentialTtl");
    openapiFields.add("otpRequired");
    openapiFields.add("passwordPattern");
    openapiFields.add("resetTokenTtl");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AuthenticationOptions
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AuthenticationOptions.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AuthenticationOptions is not found in the empty JSON string", AuthenticationOptions.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AuthenticationOptions.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AuthenticationOptions` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("passwordPattern") != null && !jsonObj.get("passwordPattern").isJsonNull()) && !jsonObj.get("passwordPattern").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `passwordPattern` to be a primitive type in the JSON string but got `%s`", jsonObj.get("passwordPattern").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AuthenticationOptions.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AuthenticationOptions' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AuthenticationOptions> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AuthenticationOptions.class));

       return (TypeAdapter<T>) new TypeAdapter<AuthenticationOptions>() {
           @Override
           public void write(JsonWriter out, AuthenticationOptions value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AuthenticationOptions read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AuthenticationOptions given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AuthenticationOptions
   * @throws IOException if the JSON string is invalid with respect to AuthenticationOptions
   */
  public static AuthenticationOptions fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AuthenticationOptions.class);
  }

  /**
   * Convert an instance of AuthenticationOptions to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

