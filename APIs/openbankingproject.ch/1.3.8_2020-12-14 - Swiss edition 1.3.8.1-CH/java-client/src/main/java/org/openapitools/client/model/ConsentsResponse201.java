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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AuthenticationObject;
import org.openapitools.client.model.ChallengeData;
import org.openapitools.client.model.ConsentStatus;
import org.openapitools.client.model.LinksConsents;

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
 * Body of the JSON response for a successful consent request.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:56.314640-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ConsentsResponse201 {
  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private LinksConsents links;

  public static final String SERIALIZED_NAME_CHALLENGE_DATA = "challengeData";
  @SerializedName(SERIALIZED_NAME_CHALLENGE_DATA)
  private ChallengeData challengeData;

  public static final String SERIALIZED_NAME_CHOSEN_SCA_METHOD = "chosenScaMethod";
  @SerializedName(SERIALIZED_NAME_CHOSEN_SCA_METHOD)
  private AuthenticationObject chosenScaMethod;

  public static final String SERIALIZED_NAME_CONSENT_ID = "consentId";
  @SerializedName(SERIALIZED_NAME_CONSENT_ID)
  private String consentId;

  public static final String SERIALIZED_NAME_CONSENT_STATUS = "consentStatus";
  @SerializedName(SERIALIZED_NAME_CONSENT_STATUS)
  private ConsentStatus consentStatus;

  public static final String SERIALIZED_NAME_PSU_MESSAGE = "psuMessage";
  @SerializedName(SERIALIZED_NAME_PSU_MESSAGE)
  private String psuMessage;

  public static final String SERIALIZED_NAME_SCA_METHODS = "scaMethods";
  @SerializedName(SERIALIZED_NAME_SCA_METHODS)
  private List<AuthenticationObject> scaMethods = new ArrayList<>();

  public ConsentsResponse201() {
  }

  public ConsentsResponse201 links(LinksConsents links) {
    this.links = links;
    return this;
  }

  /**
   * Get links
   * @return links
   */
  @javax.annotation.Nonnull
  public LinksConsents getLinks() {
    return links;
  }

  public void setLinks(LinksConsents links) {
    this.links = links;
  }


  public ConsentsResponse201 challengeData(ChallengeData challengeData) {
    this.challengeData = challengeData;
    return this;
  }

  /**
   * Get challengeData
   * @return challengeData
   */
  @javax.annotation.Nullable
  public ChallengeData getChallengeData() {
    return challengeData;
  }

  public void setChallengeData(ChallengeData challengeData) {
    this.challengeData = challengeData;
  }


  public ConsentsResponse201 chosenScaMethod(AuthenticationObject chosenScaMethod) {
    this.chosenScaMethod = chosenScaMethod;
    return this;
  }

  /**
   * Get chosenScaMethod
   * @return chosenScaMethod
   */
  @javax.annotation.Nullable
  public AuthenticationObject getChosenScaMethod() {
    return chosenScaMethod;
  }

  public void setChosenScaMethod(AuthenticationObject chosenScaMethod) {
    this.chosenScaMethod = chosenScaMethod;
  }


  public ConsentsResponse201 consentId(String consentId) {
    this.consentId = consentId;
    return this;
  }

  /**
   * ID of the corresponding consent object as returned by an account information consent request. 
   * @return consentId
   */
  @javax.annotation.Nonnull
  public String getConsentId() {
    return consentId;
  }

  public void setConsentId(String consentId) {
    this.consentId = consentId;
  }


  public ConsentsResponse201 consentStatus(ConsentStatus consentStatus) {
    this.consentStatus = consentStatus;
    return this;
  }

  /**
   * Get consentStatus
   * @return consentStatus
   */
  @javax.annotation.Nonnull
  public ConsentStatus getConsentStatus() {
    return consentStatus;
  }

  public void setConsentStatus(ConsentStatus consentStatus) {
    this.consentStatus = consentStatus;
  }


  public ConsentsResponse201 psuMessage(String psuMessage) {
    this.psuMessage = psuMessage;
    return this;
  }

  /**
   * Text to be displayed to the PSU.
   * @return psuMessage
   */
  @javax.annotation.Nullable
  public String getPsuMessage() {
    return psuMessage;
  }

  public void setPsuMessage(String psuMessage) {
    this.psuMessage = psuMessage;
  }


  public ConsentsResponse201 scaMethods(List<AuthenticationObject> scaMethods) {
    this.scaMethods = scaMethods;
    return this;
  }

  public ConsentsResponse201 addScaMethodsItem(AuthenticationObject scaMethodsItem) {
    if (this.scaMethods == null) {
      this.scaMethods = new ArrayList<>();
    }
    this.scaMethods.add(scaMethodsItem);
    return this;
  }

  /**
   * This data element might be contained, if SCA is required and if the PSU has a choice between different authentication methods.  Depending on the risk management of the ASPSP this choice might be offered before or after the PSU has been identified with the first relevant factor, or if an access token is transported.  If this data element is contained, then there is also a hyperlink of type &#39;startAuthorisationWithAuthenticationMethodSelection&#39; contained in the response body.  These methods shall be presented towards the PSU for selection by the TPP. 
   * @return scaMethods
   */
  @javax.annotation.Nullable
  public List<AuthenticationObject> getScaMethods() {
    return scaMethods;
  }

  public void setScaMethods(List<AuthenticationObject> scaMethods) {
    this.scaMethods = scaMethods;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ConsentsResponse201 consentsResponse201 = (ConsentsResponse201) o;
    return Objects.equals(this.links, consentsResponse201.links) &&
        Objects.equals(this.challengeData, consentsResponse201.challengeData) &&
        Objects.equals(this.chosenScaMethod, consentsResponse201.chosenScaMethod) &&
        Objects.equals(this.consentId, consentsResponse201.consentId) &&
        Objects.equals(this.consentStatus, consentsResponse201.consentStatus) &&
        Objects.equals(this.psuMessage, consentsResponse201.psuMessage) &&
        Objects.equals(this.scaMethods, consentsResponse201.scaMethods);
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, challengeData, chosenScaMethod, consentId, consentStatus, psuMessage, scaMethods);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ConsentsResponse201 {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    challengeData: ").append(toIndentedString(challengeData)).append("\n");
    sb.append("    chosenScaMethod: ").append(toIndentedString(chosenScaMethod)).append("\n");
    sb.append("    consentId: ").append(toIndentedString(consentId)).append("\n");
    sb.append("    consentStatus: ").append(toIndentedString(consentStatus)).append("\n");
    sb.append("    psuMessage: ").append(toIndentedString(psuMessage)).append("\n");
    sb.append("    scaMethods: ").append(toIndentedString(scaMethods)).append("\n");
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
    openapiFields.add("_links");
    openapiFields.add("challengeData");
    openapiFields.add("chosenScaMethod");
    openapiFields.add("consentId");
    openapiFields.add("consentStatus");
    openapiFields.add("psuMessage");
    openapiFields.add("scaMethods");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("_links");
    openapiRequiredFields.add("consentId");
    openapiRequiredFields.add("consentStatus");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ConsentsResponse201
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ConsentsResponse201.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ConsentsResponse201 is not found in the empty JSON string", ConsentsResponse201.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ConsentsResponse201.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ConsentsResponse201` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ConsentsResponse201.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `challengeData`
      if (jsonObj.get("challengeData") != null && !jsonObj.get("challengeData").isJsonNull()) {
        ChallengeData.validateJsonElement(jsonObj.get("challengeData"));
      }
      // validate the optional field `chosenScaMethod`
      if (jsonObj.get("chosenScaMethod") != null && !jsonObj.get("chosenScaMethod").isJsonNull()) {
        AuthenticationObject.validateJsonElement(jsonObj.get("chosenScaMethod"));
      }
      if (!jsonObj.get("consentId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `consentId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("consentId").toString()));
      }
      // validate the required field `consentStatus`
      ConsentStatus.validateJsonElement(jsonObj.get("consentStatus"));
      if ((jsonObj.get("psuMessage") != null && !jsonObj.get("psuMessage").isJsonNull()) && !jsonObj.get("psuMessage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `psuMessage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("psuMessage").toString()));
      }
      if (jsonObj.get("scaMethods") != null && !jsonObj.get("scaMethods").isJsonNull()) {
        JsonArray jsonArrayscaMethods = jsonObj.getAsJsonArray("scaMethods");
        if (jsonArrayscaMethods != null) {
          // ensure the json data is an array
          if (!jsonObj.get("scaMethods").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `scaMethods` to be an array in the JSON string but got `%s`", jsonObj.get("scaMethods").toString()));
          }

          // validate the optional field `scaMethods` (array)
          for (int i = 0; i < jsonArrayscaMethods.size(); i++) {
            AuthenticationObject.validateJsonElement(jsonArrayscaMethods.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ConsentsResponse201.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ConsentsResponse201' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ConsentsResponse201> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ConsentsResponse201.class));

       return (TypeAdapter<T>) new TypeAdapter<ConsentsResponse201>() {
           @Override
           public void write(JsonWriter out, ConsentsResponse201 value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ConsentsResponse201 read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ConsentsResponse201 given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ConsentsResponse201
   * @throws IOException if the JSON string is invalid with respect to ConsentsResponse201
   */
  public static ConsentsResponse201 fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ConsentsResponse201.class);
  }

  /**
   * Convert an instance of ConsentsResponse201 to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

