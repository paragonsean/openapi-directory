/*
 * Swiss NextGen Banking API-Framework
 * # Summary The **Swiss NextGen API** is based on the NextGenPSD2 *Framework Version 1.3.4* of the Berlin Group which offers a modern, open, harmonised and interoperable set of Application Programming Interfaces (APIs) as the safest and most efficient way to provide data securely. The NextGen Framework reduces XS2A complexity and costs, addresses the problem of multiple competing standards in Europe and, aligned with the goals of the Euro Retail Payments Board, enables European banking customers to benefit from innovative products and services ('Banking as a Service') by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data.  The Swiss edtion refines the message formats specific to Switzerland and defines some matching examples.  The possible Approaches are:   * Redirect SCA Approach   * *(Not recommended by obp.ch community) OAuth SCA Approach*   * *(Not recommended by obp.ch community) Decoupled SCA Approach*   * *(Not recommended by obp.ch community) Embedded SCA Approach without SCA method*   * *(Not recommended by obp.ch community) Embedded SCA Approach with only one SCA method available*   * *(Not recommended by obp.ch community) Embedded SCA Approach with Selection of a SCA method*    Not every message defined in this API definition is necessary for all approaches.   Furthermore this API definition does not differ between methods which are mandatory, conditional, or optional   Therefore for a particular implementation of a compliant API it is only necessary to support   a certain subset of the methods defined in this API definition.    **Please have a look at the implementation guidelines if you are not sure   which message has to be used for the approach you are going to use.**  ## Some General Remarks Related to this version of the OpenAPI Specification: * **This API definition is based on the Implementation Guidelines of the [Berlin Group API](https://www.berlin-group.org/nextgenpsd2-downloads).**   It is not a replacement in any sense.   The main specification is (at the moment) always the Implementation Guidelines of the Berlin Group API. * **This API definition contains the REST-API for requests from the PISP to the ASPSP.** * **This API definition contains the messages for all different approaches defined in the Implementation Guidelines.** * According to the OpenAPI-Specification [https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md]      \"If in is \"header\" and the name field is \"Accept\", \"Content-Type\" or \"Authorization\", the parameter definition SHALL be ignored.\"    The element \"Accept\" will not be defined in this file at any place.    The elements \"Content-Type\" and \"Authorization\" are implicitly defined by the OpenApi tags \"content\" and \"security\".  * There are several predefined types which might occur in payment initiation messages,   but are not used in the standard JSON messages in the Implementation Guidelines.   Therefore they are not used in the corresponding messages in this file either.   We added them for the convenience of the user.   If there is a payment product, which needs these fields, one can easily use the predefined types.   But the ASPSP need not to accept them in general.  * **We omit the definition of all standard HTTP header elements (mandatory/optional/conditional)   except they are mentioned in the Implementation Guidelines.**   Therefore the implementer might add these in his own realisation of a comlient API in addition to the elements defined in this file.  ## General Remarks on Data Types  The Berlin Group definition of UTF-8 strings in context of the API have to support at least the following characters  a b c d e f g h i j k l m n o p q r s t u v w x y z  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  0 1 2 3 4 5 6 7 8 9  / - ? : ( ) . , ' +  Space 
 *
 * The version of the OpenAPI document: 1.3.8_2020-12-14 - Swiss edition 1.3.8.1-CH
 * Contact: info@obp.ch
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
import org.openapitools.client.model.HrefType;

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
 * A list of hyperlinks to be recognised by the TPP. Might be contained, if several authentication methods are available for the PSU. Type of links admitted in this response:   * &#39;updateAdditionalPsuAuthentication&#39;:     The link to the payment initiation or account information resource,     which needs to be updated by an additional PSU password.     This link is only contained in rare cases,     where such additional passwords are needed for PSU authentications.   * &#39;updateAdditionalEncryptedPsuAuthentication&#39;:     The link to the payment initiation or account information resource,     which needs to be updated by an additional encrypted PSU password.     This link is only contained in rare cases, where such additional passwords are needed for PSU authentications.   * &#39;selectAuthenticationMethod&#39;:     This is a link to a resource, where the TPP can select the applicable second factor authentication     methods for the PSU, if there were several available authentication methods.     This link is only contained, if the PSU is already identified or authenticated with the first relevant     factor or alternatively an access token, if SCA is required and if the PSU has a choice between different     authentication methods.     If this link is contained, then there is also the data element &#39;scaMethods&#39; contained in the response body.   * &#39;authoriseTransaction&#39;:      The link to the resource, where the \&quot;Transaction authorisation request\&quot; is sent to.      This is the link to the resource which will authorise the transaction by checking the SCA authentication      data within the Embedded SCA approach.   * &#39;scaStatus&#39;:     The link to retrieve the scaStatus of the corresponding authorisation sub-resource. 
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:56.314640-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class LinksUpdatePsuAuthentication {
  public static final String SERIALIZED_NAME_AUTHORISE_TRANSACTION = "authoriseTransaction";
  @SerializedName(SERIALIZED_NAME_AUTHORISE_TRANSACTION)
  private HrefType authoriseTransaction;

  public static final String SERIALIZED_NAME_SCA_STATUS = "scaStatus";
  @SerializedName(SERIALIZED_NAME_SCA_STATUS)
  private HrefType scaStatus;

  public static final String SERIALIZED_NAME_SELECT_AUTHENTICATION_METHOD = "selectAuthenticationMethod";
  @SerializedName(SERIALIZED_NAME_SELECT_AUTHENTICATION_METHOD)
  private HrefType selectAuthenticationMethod;

  public static final String SERIALIZED_NAME_UPDATE_ADDITIONAL_ENCRYPTED_PSU_AUTHENTICATION = "updateAdditionalEncryptedPsuAuthentication";
  @SerializedName(SERIALIZED_NAME_UPDATE_ADDITIONAL_ENCRYPTED_PSU_AUTHENTICATION)
  private HrefType updateAdditionalEncryptedPsuAuthentication;

  public static final String SERIALIZED_NAME_UPDATE_ADDITIONAL_PSU_AUTHENTICATION = "updateAdditionalPsuAuthentication";
  @SerializedName(SERIALIZED_NAME_UPDATE_ADDITIONAL_PSU_AUTHENTICATION)
  private HrefType updateAdditionalPsuAuthentication;

  public LinksUpdatePsuAuthentication() {
  }

  public LinksUpdatePsuAuthentication authoriseTransaction(HrefType authoriseTransaction) {
    this.authoriseTransaction = authoriseTransaction;
    return this;
  }

  /**
   * Get authoriseTransaction
   * @return authoriseTransaction
   */
  @javax.annotation.Nullable
  public HrefType getAuthoriseTransaction() {
    return authoriseTransaction;
  }

  public void setAuthoriseTransaction(HrefType authoriseTransaction) {
    this.authoriseTransaction = authoriseTransaction;
  }


  public LinksUpdatePsuAuthentication scaStatus(HrefType scaStatus) {
    this.scaStatus = scaStatus;
    return this;
  }

  /**
   * Get scaStatus
   * @return scaStatus
   */
  @javax.annotation.Nullable
  public HrefType getScaStatus() {
    return scaStatus;
  }

  public void setScaStatus(HrefType scaStatus) {
    this.scaStatus = scaStatus;
  }


  public LinksUpdatePsuAuthentication selectAuthenticationMethod(HrefType selectAuthenticationMethod) {
    this.selectAuthenticationMethod = selectAuthenticationMethod;
    return this;
  }

  /**
   * Get selectAuthenticationMethod
   * @return selectAuthenticationMethod
   */
  @javax.annotation.Nullable
  public HrefType getSelectAuthenticationMethod() {
    return selectAuthenticationMethod;
  }

  public void setSelectAuthenticationMethod(HrefType selectAuthenticationMethod) {
    this.selectAuthenticationMethod = selectAuthenticationMethod;
  }


  public LinksUpdatePsuAuthentication updateAdditionalEncryptedPsuAuthentication(HrefType updateAdditionalEncryptedPsuAuthentication) {
    this.updateAdditionalEncryptedPsuAuthentication = updateAdditionalEncryptedPsuAuthentication;
    return this;
  }

  /**
   * Get updateAdditionalEncryptedPsuAuthentication
   * @return updateAdditionalEncryptedPsuAuthentication
   */
  @javax.annotation.Nullable
  public HrefType getUpdateAdditionalEncryptedPsuAuthentication() {
    return updateAdditionalEncryptedPsuAuthentication;
  }

  public void setUpdateAdditionalEncryptedPsuAuthentication(HrefType updateAdditionalEncryptedPsuAuthentication) {
    this.updateAdditionalEncryptedPsuAuthentication = updateAdditionalEncryptedPsuAuthentication;
  }


  public LinksUpdatePsuAuthentication updateAdditionalPsuAuthentication(HrefType updateAdditionalPsuAuthentication) {
    this.updateAdditionalPsuAuthentication = updateAdditionalPsuAuthentication;
    return this;
  }

  /**
   * Get updateAdditionalPsuAuthentication
   * @return updateAdditionalPsuAuthentication
   */
  @javax.annotation.Nullable
  public HrefType getUpdateAdditionalPsuAuthentication() {
    return updateAdditionalPsuAuthentication;
  }

  public void setUpdateAdditionalPsuAuthentication(HrefType updateAdditionalPsuAuthentication) {
    this.updateAdditionalPsuAuthentication = updateAdditionalPsuAuthentication;
  }

  /**
   * A container for additional, undeclared properties.
   * This is a holder for any undeclared properties as specified with
   * the 'additionalProperties' keyword in the OAS document.
   */
  private Map<String, Object> additionalProperties;

  /**
   * Set the additional (undeclared) property with the specified name and value.
   * If the property does not already exist, create it otherwise replace it.
   *
   * @param key name of the property
   * @param value value of the property
   * @return the LinksUpdatePsuAuthentication instance itself
   */
  public LinksUpdatePsuAuthentication putAdditionalProperty(String key, Object value) {
    if (this.additionalProperties == null) {
        this.additionalProperties = new HashMap<String, Object>();
    }
    this.additionalProperties.put(key, value);
    return this;
  }

  /**
   * Return the additional (undeclared) property.
   *
   * @return a map of objects
   */
  public Map<String, Object> getAdditionalProperties() {
    return additionalProperties;
  }

  /**
   * Return the additional (undeclared) property with the specified name.
   *
   * @param key name of the property
   * @return an object
   */
  public Object getAdditionalProperty(String key) {
    if (this.additionalProperties == null) {
        return null;
    }
    return this.additionalProperties.get(key);
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    LinksUpdatePsuAuthentication linksUpdatePsuAuthentication = (LinksUpdatePsuAuthentication) o;
    return Objects.equals(this.authoriseTransaction, linksUpdatePsuAuthentication.authoriseTransaction) &&
        Objects.equals(this.scaStatus, linksUpdatePsuAuthentication.scaStatus) &&
        Objects.equals(this.selectAuthenticationMethod, linksUpdatePsuAuthentication.selectAuthenticationMethod) &&
        Objects.equals(this.updateAdditionalEncryptedPsuAuthentication, linksUpdatePsuAuthentication.updateAdditionalEncryptedPsuAuthentication) &&
        Objects.equals(this.updateAdditionalPsuAuthentication, linksUpdatePsuAuthentication.updateAdditionalPsuAuthentication)&&
        Objects.equals(this.additionalProperties, linksUpdatePsuAuthentication.additionalProperties);
  }

  @Override
  public int hashCode() {
    return Objects.hash(authoriseTransaction, scaStatus, selectAuthenticationMethod, updateAdditionalEncryptedPsuAuthentication, updateAdditionalPsuAuthentication, additionalProperties);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class LinksUpdatePsuAuthentication {\n");
    sb.append("    authoriseTransaction: ").append(toIndentedString(authoriseTransaction)).append("\n");
    sb.append("    scaStatus: ").append(toIndentedString(scaStatus)).append("\n");
    sb.append("    selectAuthenticationMethod: ").append(toIndentedString(selectAuthenticationMethod)).append("\n");
    sb.append("    updateAdditionalEncryptedPsuAuthentication: ").append(toIndentedString(updateAdditionalEncryptedPsuAuthentication)).append("\n");
    sb.append("    updateAdditionalPsuAuthentication: ").append(toIndentedString(updateAdditionalPsuAuthentication)).append("\n");
    sb.append("    additionalProperties: ").append(toIndentedString(additionalProperties)).append("\n");
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
    openapiFields.add("authoriseTransaction");
    openapiFields.add("scaStatus");
    openapiFields.add("selectAuthenticationMethod");
    openapiFields.add("updateAdditionalEncryptedPsuAuthentication");
    openapiFields.add("updateAdditionalPsuAuthentication");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to LinksUpdatePsuAuthentication
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!LinksUpdatePsuAuthentication.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in LinksUpdatePsuAuthentication is not found in the empty JSON string", LinksUpdatePsuAuthentication.openapiRequiredFields.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `authoriseTransaction`
      if (jsonObj.get("authoriseTransaction") != null && !jsonObj.get("authoriseTransaction").isJsonNull()) {
        HrefType.validateJsonElement(jsonObj.get("authoriseTransaction"));
      }
      // validate the optional field `scaStatus`
      if (jsonObj.get("scaStatus") != null && !jsonObj.get("scaStatus").isJsonNull()) {
        HrefType.validateJsonElement(jsonObj.get("scaStatus"));
      }
      // validate the optional field `selectAuthenticationMethod`
      if (jsonObj.get("selectAuthenticationMethod") != null && !jsonObj.get("selectAuthenticationMethod").isJsonNull()) {
        HrefType.validateJsonElement(jsonObj.get("selectAuthenticationMethod"));
      }
      // validate the optional field `updateAdditionalEncryptedPsuAuthentication`
      if (jsonObj.get("updateAdditionalEncryptedPsuAuthentication") != null && !jsonObj.get("updateAdditionalEncryptedPsuAuthentication").isJsonNull()) {
        HrefType.validateJsonElement(jsonObj.get("updateAdditionalEncryptedPsuAuthentication"));
      }
      // validate the optional field `updateAdditionalPsuAuthentication`
      if (jsonObj.get("updateAdditionalPsuAuthentication") != null && !jsonObj.get("updateAdditionalPsuAuthentication").isJsonNull()) {
        HrefType.validateJsonElement(jsonObj.get("updateAdditionalPsuAuthentication"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!LinksUpdatePsuAuthentication.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'LinksUpdatePsuAuthentication' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<LinksUpdatePsuAuthentication> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(LinksUpdatePsuAuthentication.class));

       return (TypeAdapter<T>) new TypeAdapter<LinksUpdatePsuAuthentication>() {
           @Override
           public void write(JsonWriter out, LinksUpdatePsuAuthentication value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             obj.remove("additionalProperties");
             // serialize additional properties
             if (value.getAdditionalProperties() != null) {
               for (Map.Entry<String, Object> entry : value.getAdditionalProperties().entrySet()) {
                 if (entry.getValue() instanceof String)
                   obj.addProperty(entry.getKey(), (String) entry.getValue());
                 else if (entry.getValue() instanceof Number)
                   obj.addProperty(entry.getKey(), (Number) entry.getValue());
                 else if (entry.getValue() instanceof Boolean)
                   obj.addProperty(entry.getKey(), (Boolean) entry.getValue());
                 else if (entry.getValue() instanceof Character)
                   obj.addProperty(entry.getKey(), (Character) entry.getValue());
                 else {
                   JsonElement jsonElement = gson.toJsonTree(entry.getValue());
                   if (jsonElement.isJsonArray()) {
                     obj.add(entry.getKey(), jsonElement.getAsJsonArray());
                   } else {
                     obj.add(entry.getKey(), jsonElement.getAsJsonObject());
                   }
                 }
               }
             }
             elementAdapter.write(out, obj);
           }

           @Override
           public LinksUpdatePsuAuthentication read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             JsonObject jsonObj = jsonElement.getAsJsonObject();
             // store additional fields in the deserialized instance
             LinksUpdatePsuAuthentication instance = thisAdapter.fromJsonTree(jsonObj);
             for (Map.Entry<String, JsonElement> entry : jsonObj.entrySet()) {
               if (!openapiFields.contains(entry.getKey())) {
                 if (entry.getValue().isJsonPrimitive()) { // primitive type
                   if (entry.getValue().getAsJsonPrimitive().isString())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsString());
                   else if (entry.getValue().getAsJsonPrimitive().isNumber())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsNumber());
                   else if (entry.getValue().getAsJsonPrimitive().isBoolean())
                     instance.putAdditionalProperty(entry.getKey(), entry.getValue().getAsBoolean());
                   else
                     throw new IllegalArgumentException(String.format("The field `%s` has unknown primitive type. Value: %s", entry.getKey(), entry.getValue().toString()));
                 } else if (entry.getValue().isJsonArray()) {
                     instance.putAdditionalProperty(entry.getKey(), gson.fromJson(entry.getValue(), List.class));
                 } else { // JSON object
                     instance.putAdditionalProperty(entry.getKey(), gson.fromJson(entry.getValue(), HashMap.class));
                 }
               }
             }
             return instance;
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of LinksUpdatePsuAuthentication given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of LinksUpdatePsuAuthentication
   * @throws IOException if the JSON string is invalid with respect to LinksUpdatePsuAuthentication
   */
  public static LinksUpdatePsuAuthentication fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, LinksUpdatePsuAuthentication.class);
  }

  /**
   * Convert an instance of LinksUpdatePsuAuthentication to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

