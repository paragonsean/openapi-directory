/*
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
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
 * Represents an opted out contact
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:09.684594-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DoNotContact {
  public static final String SERIALIZED_NAME_CALL = "call";
  @SerializedName(SERIALIZED_NAME_CALL)
  private Boolean call;

  public static final String SERIALIZED_NAME_CAMPAIGN_ID = "campaignId";
  @SerializedName(SERIALIZED_NAME_CAMPAIGN_ID)
  private Long campaignId;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private Long created;

  public static final String SERIALIZED_NAME_INBOUND_CALL = "inboundCall";
  @SerializedName(SERIALIZED_NAME_INBOUND_CALL)
  private Boolean inboundCall;

  public static final String SERIALIZED_NAME_INBOUND_TEXT = "inboundText";
  @SerializedName(SERIALIZED_NAME_INBOUND_TEXT)
  private Boolean inboundText;

  public static final String SERIALIZED_NAME_NUMBER = "number";
  @SerializedName(SERIALIZED_NAME_NUMBER)
  private String number;

  public static final String SERIALIZED_NAME_SOURCE = "source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private String source;

  public static final String SERIALIZED_NAME_TEXT = "text";
  @SerializedName(SERIALIZED_NAME_TEXT)
  private Boolean text;

  public DoNotContact() {
  }

  public DoNotContact(
     Long campaignId, 
     Long created
  ) {
    this();
    this.campaignId = campaignId;
    this.created = created;
  }

  public DoNotContact call(Boolean call) {
    this.call = call;
    return this;
  }

  /**
   * A number on Do-Not-Call list
   * @return call
   */
  @javax.annotation.Nullable
  public Boolean getCall() {
    return call;
  }

  public void setCall(Boolean call) {
    this.call = call;
  }


  /**
   * An Id of a campaign which was used to send a message to DNC number
   * @return campaignId
   */
  @javax.annotation.Nullable
  public Long getCampaignId() {
    return campaignId;
  }



  /**
   * A time when a given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
   * @return created
   */
  @javax.annotation.Nullable
  public Long getCreated() {
    return created;
  }



  public DoNotContact inboundCall(Boolean inboundCall) {
    this.inboundCall = inboundCall;
    return this;
  }

  /**
   * ~
   * @return inboundCall
   */
  @javax.annotation.Nullable
  public Boolean getInboundCall() {
    return inboundCall;
  }

  public void setInboundCall(Boolean inboundCall) {
    this.inboundCall = inboundCall;
  }


  public DoNotContact inboundText(Boolean inboundText) {
    this.inboundText = inboundText;
    return this;
  }

  /**
   * ~
   * @return inboundText
   */
  @javax.annotation.Nullable
  public Boolean getInboundText() {
    return inboundText;
  }

  public void setInboundText(Boolean inboundText) {
    this.inboundText = inboundText;
  }


  public DoNotContact number(String number) {
    this.number = number;
    return this;
  }

  /**
   * A single DNC number in E.164 format (11-digit). Example: 12132000384
   * @return number
   */
  @javax.annotation.Nullable
  public String getNumber() {
    return number;
  }

  public void setNumber(String number) {
    this.number = number;
  }


  public DoNotContact source(String source) {
    this.source = source;
    return this;
  }

  /**
   * The name of DNC source (can be the name of DNC list that user uploads to CallFire)
   * @return source
   */
  @javax.annotation.Nullable
  public String getSource() {
    return source;
  }

  public void setSource(String source) {
    this.source = source;
  }


  public DoNotContact text(Boolean text) {
    this.text = text;
    return this;
  }

  /**
   * A number on Do-Not-Text list
   * @return text
   */
  @javax.annotation.Nullable
  public Boolean getText() {
    return text;
  }

  public void setText(Boolean text) {
    this.text = text;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DoNotContact doNotContact = (DoNotContact) o;
    return Objects.equals(this.call, doNotContact.call) &&
        Objects.equals(this.campaignId, doNotContact.campaignId) &&
        Objects.equals(this.created, doNotContact.created) &&
        Objects.equals(this.inboundCall, doNotContact.inboundCall) &&
        Objects.equals(this.inboundText, doNotContact.inboundText) &&
        Objects.equals(this.number, doNotContact.number) &&
        Objects.equals(this.source, doNotContact.source) &&
        Objects.equals(this.text, doNotContact.text);
  }

  @Override
  public int hashCode() {
    return Objects.hash(call, campaignId, created, inboundCall, inboundText, number, source, text);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DoNotContact {\n");
    sb.append("    call: ").append(toIndentedString(call)).append("\n");
    sb.append("    campaignId: ").append(toIndentedString(campaignId)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    inboundCall: ").append(toIndentedString(inboundCall)).append("\n");
    sb.append("    inboundText: ").append(toIndentedString(inboundText)).append("\n");
    sb.append("    number: ").append(toIndentedString(number)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    text: ").append(toIndentedString(text)).append("\n");
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
    openapiFields.add("call");
    openapiFields.add("campaignId");
    openapiFields.add("created");
    openapiFields.add("inboundCall");
    openapiFields.add("inboundText");
    openapiFields.add("number");
    openapiFields.add("source");
    openapiFields.add("text");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DoNotContact
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DoNotContact.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DoNotContact is not found in the empty JSON string", DoNotContact.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DoNotContact.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DoNotContact` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("number") != null && !jsonObj.get("number").isJsonNull()) && !jsonObj.get("number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("number").toString()));
      }
      if ((jsonObj.get("source") != null && !jsonObj.get("source").isJsonNull()) && !jsonObj.get("source").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `source` to be a primitive type in the JSON string but got `%s`", jsonObj.get("source").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DoNotContact.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DoNotContact' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DoNotContact> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DoNotContact.class));

       return (TypeAdapter<T>) new TypeAdapter<DoNotContact>() {
           @Override
           public void write(JsonWriter out, DoNotContact value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DoNotContact read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DoNotContact given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DoNotContact
   * @throws IOException if the JSON string is invalid with respect to DoNotContact
   */
  public static DoNotContact fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DoNotContact.class);
  }

  /**
   * Convert an instance of DoNotContact to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

