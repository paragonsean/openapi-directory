/*
 * API iSendPro
 * [1] Liste des fonctionnalités : - envoi de SMS à un ou plusieurs destinataires, - lookup HLR, - récupération des récapitulatifs de campagne, - gestion des répertoires, - ajout en liste noire. - comptage du nombre de caractères des SMS  [2] Pour utiliser cette API vous devez: - Créer un compte iSendPro sur https://isendpro.com/ - Créditer votre compte      - Remarque: obtention d'un crédit de test possible sous conditions - Noter votre clé de compte (keyid)   - Elle vous sera indispensable à l'utilisation de l'API   - Vous pouvez la trouver dans le rubrique mon \"compte\", sous-rubrique \"mon API\" - Configurer le contrôle IP   - Le contrôle IP est configurable dans le rubrique mon \"compte\", sous-rubrique \"mon API\"   - Il s'agit d'un système de liste blanche, vous devez entrer les IP utilisées pour appeler l'API   - Vous pouvez également désactiver totalement le contrôle IP 
 *
 * The version of the OpenAPI document: 1.1.1
 * Contact: support@isendpro.com
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
 * SubaccountAddResponseEtatEtatInner
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:47.335301-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class SubaccountAddResponseEtatEtatInner {
  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private BigDecimal code;

  public static final String SERIALIZED_NAME_MESSAGE = "message";
  @SerializedName(SERIALIZED_NAME_MESSAGE)
  private String message;

  public static final String SERIALIZED_NAME_SUB_ACCOUNT_ID = "subAccountId";
  @SerializedName(SERIALIZED_NAME_SUB_ACCOUNT_ID)
  private String subAccountId;

  public static final String SERIALIZED_NAME_SUB_ACCOUNT_KEY_ID = "subAccountKeyId";
  @SerializedName(SERIALIZED_NAME_SUB_ACCOUNT_KEY_ID)
  private String subAccountKeyId;

  public static final String SERIALIZED_NAME_SUB_ACCOUNT_LOGIN = "subAccountLogin";
  @SerializedName(SERIALIZED_NAME_SUB_ACCOUNT_LOGIN)
  private String subAccountLogin;

  public SubaccountAddResponseEtatEtatInner() {
  }

  public SubaccountAddResponseEtatEtatInner code(BigDecimal code) {
    this.code = code;
    return this;
  }

  /**
   * Get code
   * @return code
   */
  @javax.annotation.Nullable
  public BigDecimal getCode() {
    return code;
  }

  public void setCode(BigDecimal code) {
    this.code = code;
  }


  public SubaccountAddResponseEtatEtatInner message(String message) {
    this.message = message;
    return this;
  }

  /**
   * Get message
   * @return message
   */
  @javax.annotation.Nullable
  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }


  public SubaccountAddResponseEtatEtatInner subAccountId(String subAccountId) {
    this.subAccountId = subAccountId;
    return this;
  }

  /**
   * Get subAccountId
   * @return subAccountId
   */
  @javax.annotation.Nullable
  public String getSubAccountId() {
    return subAccountId;
  }

  public void setSubAccountId(String subAccountId) {
    this.subAccountId = subAccountId;
  }


  public SubaccountAddResponseEtatEtatInner subAccountKeyId(String subAccountKeyId) {
    this.subAccountKeyId = subAccountKeyId;
    return this;
  }

  /**
   * Get subAccountKeyId
   * @return subAccountKeyId
   */
  @javax.annotation.Nullable
  public String getSubAccountKeyId() {
    return subAccountKeyId;
  }

  public void setSubAccountKeyId(String subAccountKeyId) {
    this.subAccountKeyId = subAccountKeyId;
  }


  public SubaccountAddResponseEtatEtatInner subAccountLogin(String subAccountLogin) {
    this.subAccountLogin = subAccountLogin;
    return this;
  }

  /**
   * Get subAccountLogin
   * @return subAccountLogin
   */
  @javax.annotation.Nullable
  public String getSubAccountLogin() {
    return subAccountLogin;
  }

  public void setSubAccountLogin(String subAccountLogin) {
    this.subAccountLogin = subAccountLogin;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    SubaccountAddResponseEtatEtatInner subaccountAddResponseEtatEtatInner = (SubaccountAddResponseEtatEtatInner) o;
    return Objects.equals(this.code, subaccountAddResponseEtatEtatInner.code) &&
        Objects.equals(this.message, subaccountAddResponseEtatEtatInner.message) &&
        Objects.equals(this.subAccountId, subaccountAddResponseEtatEtatInner.subAccountId) &&
        Objects.equals(this.subAccountKeyId, subaccountAddResponseEtatEtatInner.subAccountKeyId) &&
        Objects.equals(this.subAccountLogin, subaccountAddResponseEtatEtatInner.subAccountLogin);
  }

  @Override
  public int hashCode() {
    return Objects.hash(code, message, subAccountId, subAccountKeyId, subAccountLogin);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class SubaccountAddResponseEtatEtatInner {\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    message: ").append(toIndentedString(message)).append("\n");
    sb.append("    subAccountId: ").append(toIndentedString(subAccountId)).append("\n");
    sb.append("    subAccountKeyId: ").append(toIndentedString(subAccountKeyId)).append("\n");
    sb.append("    subAccountLogin: ").append(toIndentedString(subAccountLogin)).append("\n");
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
    openapiFields.add("code");
    openapiFields.add("message");
    openapiFields.add("subAccountId");
    openapiFields.add("subAccountKeyId");
    openapiFields.add("subAccountLogin");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to SubaccountAddResponseEtatEtatInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!SubaccountAddResponseEtatEtatInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in SubaccountAddResponseEtatEtatInner is not found in the empty JSON string", SubaccountAddResponseEtatEtatInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!SubaccountAddResponseEtatEtatInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `SubaccountAddResponseEtatEtatInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("message") != null && !jsonObj.get("message").isJsonNull()) && !jsonObj.get("message").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `message` to be a primitive type in the JSON string but got `%s`", jsonObj.get("message").toString()));
      }
      if ((jsonObj.get("subAccountId") != null && !jsonObj.get("subAccountId").isJsonNull()) && !jsonObj.get("subAccountId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subAccountId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subAccountId").toString()));
      }
      if ((jsonObj.get("subAccountKeyId") != null && !jsonObj.get("subAccountKeyId").isJsonNull()) && !jsonObj.get("subAccountKeyId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subAccountKeyId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subAccountKeyId").toString()));
      }
      if ((jsonObj.get("subAccountLogin") != null && !jsonObj.get("subAccountLogin").isJsonNull()) && !jsonObj.get("subAccountLogin").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `subAccountLogin` to be a primitive type in the JSON string but got `%s`", jsonObj.get("subAccountLogin").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!SubaccountAddResponseEtatEtatInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'SubaccountAddResponseEtatEtatInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<SubaccountAddResponseEtatEtatInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(SubaccountAddResponseEtatEtatInner.class));

       return (TypeAdapter<T>) new TypeAdapter<SubaccountAddResponseEtatEtatInner>() {
           @Override
           public void write(JsonWriter out, SubaccountAddResponseEtatEtatInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public SubaccountAddResponseEtatEtatInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of SubaccountAddResponseEtatEtatInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of SubaccountAddResponseEtatEtatInner
   * @throws IOException if the JSON string is invalid with respect to SubaccountAddResponseEtatEtatInner
   */
  public static SubaccountAddResponseEtatEtatInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, SubaccountAddResponseEtatEtatInner.class);
  }

  /**
   * Convert an instance of SubaccountAddResponseEtatEtatInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

