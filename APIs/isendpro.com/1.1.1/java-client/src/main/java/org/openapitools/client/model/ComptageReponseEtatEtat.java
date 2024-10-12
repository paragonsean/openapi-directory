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
 * ComptageReponseEtatEtat
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:47.335301-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ComptageReponseEtatEtat {
  public static final String SERIALIZED_NAME_NB_CARACTERE = "nb_caractere";
  @SerializedName(SERIALIZED_NAME_NB_CARACTERE)
  private String nbCaractere;

  public static final String SERIALIZED_NAME_NB_SMS = "nb_sms";
  @SerializedName(SERIALIZED_NAME_NB_SMS)
  private String nbSms;

  public static final String SERIALIZED_NAME_TEL = "tel";
  @SerializedName(SERIALIZED_NAME_TEL)
  private String tel;

  public ComptageReponseEtatEtat() {
  }

  public ComptageReponseEtatEtat nbCaractere(String nbCaractere) {
    this.nbCaractere = nbCaractere;
    return this;
  }

  /**
   * nombre de caractères
   * @return nbCaractere
   */
  @javax.annotation.Nullable
  public String getNbCaractere() {
    return nbCaractere;
  }

  public void setNbCaractere(String nbCaractere) {
    this.nbCaractere = nbCaractere;
  }


  public ComptageReponseEtatEtat nbSms(String nbSms) {
    this.nbSms = nbSms;
    return this;
  }

  /**
   * nombre de sms nécessaires
   * @return nbSms
   */
  @javax.annotation.Nullable
  public String getNbSms() {
    return nbSms;
  }

  public void setNbSms(String nbSms) {
    this.nbSms = nbSms;
  }


  public ComptageReponseEtatEtat tel(String tel) {
    this.tel = tel;
    return this;
  }

  /**
   * numéro de téléphone
   * @return tel
   */
  @javax.annotation.Nullable
  public String getTel() {
    return tel;
  }

  public void setTel(String tel) {
    this.tel = tel;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ComptageReponseEtatEtat comptageReponseEtatEtat = (ComptageReponseEtatEtat) o;
    return Objects.equals(this.nbCaractere, comptageReponseEtatEtat.nbCaractere) &&
        Objects.equals(this.nbSms, comptageReponseEtatEtat.nbSms) &&
        Objects.equals(this.tel, comptageReponseEtatEtat.tel);
  }

  @Override
  public int hashCode() {
    return Objects.hash(nbCaractere, nbSms, tel);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ComptageReponseEtatEtat {\n");
    sb.append("    nbCaractere: ").append(toIndentedString(nbCaractere)).append("\n");
    sb.append("    nbSms: ").append(toIndentedString(nbSms)).append("\n");
    sb.append("    tel: ").append(toIndentedString(tel)).append("\n");
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
    openapiFields.add("nb_caractere");
    openapiFields.add("nb_sms");
    openapiFields.add("tel");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ComptageReponseEtatEtat
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ComptageReponseEtatEtat.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ComptageReponseEtatEtat is not found in the empty JSON string", ComptageReponseEtatEtat.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ComptageReponseEtatEtat.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ComptageReponseEtatEtat` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("nb_caractere") != null && !jsonObj.get("nb_caractere").isJsonNull()) && !jsonObj.get("nb_caractere").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nb_caractere` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nb_caractere").toString()));
      }
      if ((jsonObj.get("nb_sms") != null && !jsonObj.get("nb_sms").isJsonNull()) && !jsonObj.get("nb_sms").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `nb_sms` to be a primitive type in the JSON string but got `%s`", jsonObj.get("nb_sms").toString()));
      }
      if ((jsonObj.get("tel") != null && !jsonObj.get("tel").isJsonNull()) && !jsonObj.get("tel").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tel` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tel").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ComptageReponseEtatEtat.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ComptageReponseEtatEtat' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ComptageReponseEtatEtat> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ComptageReponseEtatEtat.class));

       return (TypeAdapter<T>) new TypeAdapter<ComptageReponseEtatEtat>() {
           @Override
           public void write(JsonWriter out, ComptageReponseEtatEtat value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ComptageReponseEtatEtat read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ComptageReponseEtatEtat given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ComptageReponseEtatEtat
   * @throws IOException if the JSON string is invalid with respect to ComptageReponseEtatEtat
   */
  public static ComptageReponseEtatEtat fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ComptageReponseEtatEtat.class);
  }

  /**
   * Convert an instance of ComptageReponseEtatEtat to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

