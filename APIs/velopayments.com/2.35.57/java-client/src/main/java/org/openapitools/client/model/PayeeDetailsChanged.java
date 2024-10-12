/*
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.UUID;
import org.openapitools.client.model.PayeeEventAllOfReasons;

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
 * Base type for all payee details changed events
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:55.204956-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PayeeDetailsChanged {
  public static final String SERIALIZED_NAME_CREATED_AT = "createdAt";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private OffsetDateTime createdAt;

  public static final String SERIALIZED_NAME_EVENT_ID = "eventId";
  @SerializedName(SERIALIZED_NAME_EVENT_ID)
  private UUID eventId;

  public static final String SERIALIZED_NAME_SOURCE_TYPE = "sourceType";
  @SerializedName(SERIALIZED_NAME_SOURCE_TYPE)
  private String sourceType;

  public static final String SERIALIZED_NAME_PAYEE_ID = "payeeId";
  @SerializedName(SERIALIZED_NAME_PAYEE_ID)
  private UUID payeeId;

  public static final String SERIALIZED_NAME_REASONS = "reasons";
  @SerializedName(SERIALIZED_NAME_REASONS)
  private List<PayeeEventAllOfReasons> reasons = new ArrayList<>();

  public PayeeDetailsChanged() {
  }

  public PayeeDetailsChanged createdAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * ISO8601 timestamp indicating when the source event was created
   * @return createdAt
   */
  @javax.annotation.Nonnull
  public OffsetDateTime getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(OffsetDateTime createdAt) {
    this.createdAt = createdAt;
  }


  public PayeeDetailsChanged eventId(UUID eventId) {
    this.eventId = eventId;
    return this;
  }

  /**
   * UUID id of the source event in the Velo platform
   * @return eventId
   */
  @javax.annotation.Nonnull
  public UUID getEventId() {
    return eventId;
  }

  public void setEventId(UUID eventId) {
    this.eventId = eventId;
  }


  public PayeeDetailsChanged sourceType(String sourceType) {
    this.sourceType = sourceType;
    return this;
  }

  /**
   * OA3 Schema type name for the source info which is used as the discriminator value to ensure that data binding works correctly
   * @return sourceType
   */
  @javax.annotation.Nonnull
  public String getSourceType() {
    return sourceType;
  }

  public void setSourceType(String sourceType) {
    this.sourceType = sourceType;
  }


  public PayeeDetailsChanged payeeId(UUID payeeId) {
    this.payeeId = payeeId;
    return this;
  }

  /**
   * ID of this payee within the Velo platform
   * @return payeeId
   */
  @javax.annotation.Nonnull
  public UUID getPayeeId() {
    return payeeId;
  }

  public void setPayeeId(UUID payeeId) {
    this.payeeId = payeeId;
  }


  public PayeeDetailsChanged reasons(List<PayeeEventAllOfReasons> reasons) {
    this.reasons = reasons;
    return this;
  }

  public PayeeDetailsChanged addReasonsItem(PayeeEventAllOfReasons reasonsItem) {
    if (this.reasons == null) {
      this.reasons = new ArrayList<>();
    }
    this.reasons.add(reasonsItem);
    return this;
  }

  /**
   * The reasons for the event notification.
   * @return reasons
   */
  @javax.annotation.Nullable
  public List<PayeeEventAllOfReasons> getReasons() {
    return reasons;
  }

  public void setReasons(List<PayeeEventAllOfReasons> reasons) {
    this.reasons = reasons;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PayeeDetailsChanged payeeDetailsChanged = (PayeeDetailsChanged) o;
    return Objects.equals(this.createdAt, payeeDetailsChanged.createdAt) &&
        Objects.equals(this.eventId, payeeDetailsChanged.eventId) &&
        Objects.equals(this.sourceType, payeeDetailsChanged.sourceType) &&
        Objects.equals(this.payeeId, payeeDetailsChanged.payeeId) &&
        Objects.equals(this.reasons, payeeDetailsChanged.reasons);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, eventId, sourceType, payeeId, reasons);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PayeeDetailsChanged {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    eventId: ").append(toIndentedString(eventId)).append("\n");
    sb.append("    sourceType: ").append(toIndentedString(sourceType)).append("\n");
    sb.append("    payeeId: ").append(toIndentedString(payeeId)).append("\n");
    sb.append("    reasons: ").append(toIndentedString(reasons)).append("\n");
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
    openapiFields.add("createdAt");
    openapiFields.add("eventId");
    openapiFields.add("sourceType");
    openapiFields.add("payeeId");
    openapiFields.add("reasons");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("createdAt");
    openapiRequiredFields.add("eventId");
    openapiRequiredFields.add("sourceType");
    openapiRequiredFields.add("payeeId");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PayeeDetailsChanged
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PayeeDetailsChanged.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PayeeDetailsChanged is not found in the empty JSON string", PayeeDetailsChanged.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PayeeDetailsChanged.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PayeeDetailsChanged` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : PayeeDetailsChanged.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (!jsonObj.get("eventId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `eventId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("eventId").toString()));
      }
      if (!jsonObj.get("sourceType").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sourceType` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sourceType").toString()));
      }
      if (!jsonObj.get("payeeId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payeeId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payeeId").toString()));
      }
      if (jsonObj.get("reasons") != null && !jsonObj.get("reasons").isJsonNull()) {
        JsonArray jsonArrayreasons = jsonObj.getAsJsonArray("reasons");
        if (jsonArrayreasons != null) {
          // ensure the json data is an array
          if (!jsonObj.get("reasons").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `reasons` to be an array in the JSON string but got `%s`", jsonObj.get("reasons").toString()));
          }

          // validate the optional field `reasons` (array)
          for (int i = 0; i < jsonArrayreasons.size(); i++) {
            PayeeEventAllOfReasons.validateJsonElement(jsonArrayreasons.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PayeeDetailsChanged.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PayeeDetailsChanged' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PayeeDetailsChanged> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PayeeDetailsChanged.class));

       return (TypeAdapter<T>) new TypeAdapter<PayeeDetailsChanged>() {
           @Override
           public void write(JsonWriter out, PayeeDetailsChanged value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PayeeDetailsChanged read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PayeeDetailsChanged given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PayeeDetailsChanged
   * @throws IOException if the JSON string is invalid with respect to PayeeDetailsChanged
   */
  public static PayeeDetailsChanged fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PayeeDetailsChanged.class);
  }

  /**
   * Convert an instance of PayeeDetailsChanged to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

