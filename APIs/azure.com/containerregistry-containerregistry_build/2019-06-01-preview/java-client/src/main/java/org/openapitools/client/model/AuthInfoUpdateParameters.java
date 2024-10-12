/*
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-06-01-preview
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
 * The authorization properties for accessing the source code repository.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:55.681670-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AuthInfoUpdateParameters {
  public static final String SERIALIZED_NAME_EXPIRES_IN = "expiresIn";
  @SerializedName(SERIALIZED_NAME_EXPIRES_IN)
  private Integer expiresIn;

  public static final String SERIALIZED_NAME_REFRESH_TOKEN = "refreshToken";
  @SerializedName(SERIALIZED_NAME_REFRESH_TOKEN)
  private String refreshToken;

  public static final String SERIALIZED_NAME_SCOPE = "scope";
  @SerializedName(SERIALIZED_NAME_SCOPE)
  private String scope;

  public static final String SERIALIZED_NAME_TOKEN = "token";
  @SerializedName(SERIALIZED_NAME_TOKEN)
  private String token;

  /**
   * The type of Auth token.
   */
  @JsonAdapter(TokenTypeEnum.Adapter.class)
  public enum TokenTypeEnum {
    PAT("PAT"),
    
    O_AUTH("OAuth");

    private String value;

    TokenTypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TokenTypeEnum fromValue(String value) {
      for (TokenTypeEnum b : TokenTypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TokenTypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TokenTypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TokenTypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TokenTypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TokenTypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TOKEN_TYPE = "tokenType";
  @SerializedName(SERIALIZED_NAME_TOKEN_TYPE)
  private TokenTypeEnum tokenType;

  public AuthInfoUpdateParameters() {
  }

  public AuthInfoUpdateParameters expiresIn(Integer expiresIn) {
    this.expiresIn = expiresIn;
    return this;
  }

  /**
   * Time in seconds that the token remains valid
   * @return expiresIn
   */
  @javax.annotation.Nullable
  public Integer getExpiresIn() {
    return expiresIn;
  }

  public void setExpiresIn(Integer expiresIn) {
    this.expiresIn = expiresIn;
  }


  public AuthInfoUpdateParameters refreshToken(String refreshToken) {
    this.refreshToken = refreshToken;
    return this;
  }

  /**
   * The refresh token used to refresh the access token.
   * @return refreshToken
   */
  @javax.annotation.Nullable
  public String getRefreshToken() {
    return refreshToken;
  }

  public void setRefreshToken(String refreshToken) {
    this.refreshToken = refreshToken;
  }


  public AuthInfoUpdateParameters scope(String scope) {
    this.scope = scope;
    return this;
  }

  /**
   * The scope of the access token.
   * @return scope
   */
  @javax.annotation.Nullable
  public String getScope() {
    return scope;
  }

  public void setScope(String scope) {
    this.scope = scope;
  }


  public AuthInfoUpdateParameters token(String token) {
    this.token = token;
    return this;
  }

  /**
   * The access token used to access the source control provider.
   * @return token
   */
  @javax.annotation.Nullable
  public String getToken() {
    return token;
  }

  public void setToken(String token) {
    this.token = token;
  }


  public AuthInfoUpdateParameters tokenType(TokenTypeEnum tokenType) {
    this.tokenType = tokenType;
    return this;
  }

  /**
   * The type of Auth token.
   * @return tokenType
   */
  @javax.annotation.Nullable
  public TokenTypeEnum getTokenType() {
    return tokenType;
  }

  public void setTokenType(TokenTypeEnum tokenType) {
    this.tokenType = tokenType;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AuthInfoUpdateParameters authInfoUpdateParameters = (AuthInfoUpdateParameters) o;
    return Objects.equals(this.expiresIn, authInfoUpdateParameters.expiresIn) &&
        Objects.equals(this.refreshToken, authInfoUpdateParameters.refreshToken) &&
        Objects.equals(this.scope, authInfoUpdateParameters.scope) &&
        Objects.equals(this.token, authInfoUpdateParameters.token) &&
        Objects.equals(this.tokenType, authInfoUpdateParameters.tokenType);
  }

  @Override
  public int hashCode() {
    return Objects.hash(expiresIn, refreshToken, scope, token, tokenType);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AuthInfoUpdateParameters {\n");
    sb.append("    expiresIn: ").append(toIndentedString(expiresIn)).append("\n");
    sb.append("    refreshToken: ").append(toIndentedString(refreshToken)).append("\n");
    sb.append("    scope: ").append(toIndentedString(scope)).append("\n");
    sb.append("    token: ").append(toIndentedString(token)).append("\n");
    sb.append("    tokenType: ").append(toIndentedString(tokenType)).append("\n");
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
    openapiFields.add("expiresIn");
    openapiFields.add("refreshToken");
    openapiFields.add("scope");
    openapiFields.add("token");
    openapiFields.add("tokenType");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AuthInfoUpdateParameters
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AuthInfoUpdateParameters.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AuthInfoUpdateParameters is not found in the empty JSON string", AuthInfoUpdateParameters.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AuthInfoUpdateParameters.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AuthInfoUpdateParameters` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("refreshToken") != null && !jsonObj.get("refreshToken").isJsonNull()) && !jsonObj.get("refreshToken").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `refreshToken` to be a primitive type in the JSON string but got `%s`", jsonObj.get("refreshToken").toString()));
      }
      if ((jsonObj.get("scope") != null && !jsonObj.get("scope").isJsonNull()) && !jsonObj.get("scope").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scope` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scope").toString()));
      }
      if ((jsonObj.get("token") != null && !jsonObj.get("token").isJsonNull()) && !jsonObj.get("token").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `token` to be a primitive type in the JSON string but got `%s`", jsonObj.get("token").toString()));
      }
      if ((jsonObj.get("tokenType") != null && !jsonObj.get("tokenType").isJsonNull()) && !jsonObj.get("tokenType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tokenType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tokenType").toString()));
      }
      // validate the optional field `tokenType`
      if (jsonObj.get("tokenType") != null && !jsonObj.get("tokenType").isJsonNull()) {
        TokenTypeEnum.validateJsonElement(jsonObj.get("tokenType"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AuthInfoUpdateParameters.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AuthInfoUpdateParameters' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AuthInfoUpdateParameters> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AuthInfoUpdateParameters.class));

       return (TypeAdapter<T>) new TypeAdapter<AuthInfoUpdateParameters>() {
           @Override
           public void write(JsonWriter out, AuthInfoUpdateParameters value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AuthInfoUpdateParameters read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AuthInfoUpdateParameters given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AuthInfoUpdateParameters
   * @throws IOException if the JSON string is invalid with respect to AuthInfoUpdateParameters
   */
  public static AuthInfoUpdateParameters fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AuthInfoUpdateParameters.class);
  }

  /**
   * Convert an instance of AuthInfoUpdateParameters to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

