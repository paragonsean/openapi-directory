/*
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
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
import org.openapitools.client.model.Consumer;
import org.openapitools.client.model.Rights;

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
 * Token
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:19.318125-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Token {
  public static final String SERIALIZED_NAME_CONSUMER = "consumer";
  @SerializedName(SERIALIZED_NAME_CONSUMER)
  private Consumer consumer;

  public static final String SERIALIZED_NAME_CREATION_DATE = "creationDate";
  @SerializedName(SERIALIZED_NAME_CREATION_DATE)
  private Integer creationDate;

  public static final String SERIALIZED_NAME_LAST_UTILISATION = "lastUtilisation";
  @SerializedName(SERIALIZED_NAME_LAST_UTILISATION)
  private String lastUtilisation;

  public static final String SERIALIZED_NAME_RIGHTS = "rights";
  @SerializedName(SERIALIZED_NAME_RIGHTS)
  private Rights rights;

  public static final String SERIALIZED_NAME_TOKEN = "token";
  @SerializedName(SERIALIZED_NAME_TOKEN)
  private String token;

  public Token() {
  }

  public Token consumer(Consumer consumer) {
    this.consumer = consumer;
    return this;
  }

  /**
   * Get consumer
   * @return consumer
   */
  @javax.annotation.Nonnull
  public Consumer getConsumer() {
    return consumer;
  }

  public void setConsumer(Consumer consumer) {
    this.consumer = consumer;
  }


  public Token creationDate(Integer creationDate) {
    this.creationDate = creationDate;
    return this;
  }

  /**
   * Get creationDate
   * @return creationDate
   */
  @javax.annotation.Nonnull
  public Integer getCreationDate() {
    return creationDate;
  }

  public void setCreationDate(Integer creationDate) {
    this.creationDate = creationDate;
  }


  public Token lastUtilisation(String lastUtilisation) {
    this.lastUtilisation = lastUtilisation;
    return this;
  }

  /**
   * Get lastUtilisation
   * @return lastUtilisation
   */
  @javax.annotation.Nonnull
  public String getLastUtilisation() {
    return lastUtilisation;
  }

  public void setLastUtilisation(String lastUtilisation) {
    this.lastUtilisation = lastUtilisation;
  }


  public Token rights(Rights rights) {
    this.rights = rights;
    return this;
  }

  /**
   * Get rights
   * @return rights
   */
  @javax.annotation.Nonnull
  public Rights getRights() {
    return rights;
  }

  public void setRights(Rights rights) {
    this.rights = rights;
  }


  public Token token(String token) {
    this.token = token;
    return this;
  }

  /**
   * Get token
   * @return token
   */
  @javax.annotation.Nonnull
  public String getToken() {
    return token;
  }

  public void setToken(String token) {
    this.token = token;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Token token = (Token) o;
    return Objects.equals(this.consumer, token.consumer) &&
        Objects.equals(this.creationDate, token.creationDate) &&
        Objects.equals(this.lastUtilisation, token.lastUtilisation) &&
        Objects.equals(this.rights, token.rights) &&
        Objects.equals(this.token, token.token);
  }

  @Override
  public int hashCode() {
    return Objects.hash(consumer, creationDate, lastUtilisation, rights, token);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Token {\n");
    sb.append("    consumer: ").append(toIndentedString(consumer)).append("\n");
    sb.append("    creationDate: ").append(toIndentedString(creationDate)).append("\n");
    sb.append("    lastUtilisation: ").append(toIndentedString(lastUtilisation)).append("\n");
    sb.append("    rights: ").append(toIndentedString(rights)).append("\n");
    sb.append("    token: ").append(toIndentedString(token)).append("\n");
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
    openapiFields.add("consumer");
    openapiFields.add("creationDate");
    openapiFields.add("lastUtilisation");
    openapiFields.add("rights");
    openapiFields.add("token");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("consumer");
    openapiRequiredFields.add("creationDate");
    openapiRequiredFields.add("lastUtilisation");
    openapiRequiredFields.add("rights");
    openapiRequiredFields.add("token");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Token
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Token.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Token is not found in the empty JSON string", Token.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Token.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Token` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Token.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the required field `consumer`
      Consumer.validateJsonElement(jsonObj.get("consumer"));
      if (!jsonObj.get("lastUtilisation").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lastUtilisation` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lastUtilisation").toString()));
      }
      // validate the required field `rights`
      Rights.validateJsonElement(jsonObj.get("rights"));
      if (!jsonObj.get("token").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `token` to be a primitive type in the JSON string but got `%s`", jsonObj.get("token").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Token.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Token' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Token> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Token.class));

       return (TypeAdapter<T>) new TypeAdapter<Token>() {
           @Override
           public void write(JsonWriter out, Token value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Token read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Token given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Token
   * @throws IOException if the JSON string is invalid with respect to Token
   */
  public static Token fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Token.class);
  }

  /**
   * Convert an instance of Token to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

