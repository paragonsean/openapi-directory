/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CreateOrganizationActionBatchRequestActionsInner;

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
 * CreateOrganizationActionBatchRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:58:52.491325-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CreateOrganizationActionBatchRequest {
  public static final String SERIALIZED_NAME_ACTIONS = "actions";
  @SerializedName(SERIALIZED_NAME_ACTIONS)
  private List<CreateOrganizationActionBatchRequestActionsInner> actions = new ArrayList<>();

  public static final String SERIALIZED_NAME_CONFIRMED = "confirmed";
  @SerializedName(SERIALIZED_NAME_CONFIRMED)
  private Boolean confirmed;

  public static final String SERIALIZED_NAME_SYNCHRONOUS = "synchronous";
  @SerializedName(SERIALIZED_NAME_SYNCHRONOUS)
  private Boolean synchronous;

  public CreateOrganizationActionBatchRequest() {
  }

  public CreateOrganizationActionBatchRequest actions(List<CreateOrganizationActionBatchRequestActionsInner> actions) {
    this.actions = actions;
    return this;
  }

  public CreateOrganizationActionBatchRequest addActionsItem(CreateOrganizationActionBatchRequestActionsInner actionsItem) {
    if (this.actions == null) {
      this.actions = new ArrayList<>();
    }
    this.actions.add(actionsItem);
    return this;
  }

  /**
   * A set of changes to make as part of this action (&lt;a href&#x3D;&#39;https://developer.cisco.com/meraki/api/#/rest/guides/action-batches/&#39;&gt;more details&lt;/a&gt;)
   * @return actions
   */
  @javax.annotation.Nonnull
  public List<CreateOrganizationActionBatchRequestActionsInner> getActions() {
    return actions;
  }

  public void setActions(List<CreateOrganizationActionBatchRequestActionsInner> actions) {
    this.actions = actions;
  }


  public CreateOrganizationActionBatchRequest confirmed(Boolean confirmed) {
    this.confirmed = confirmed;
    return this;
  }

  /**
   * Set to true for immediate execution. Set to false if the action should be previewed before executing. This property cannot be unset once it is true. Defaults to false.
   * @return confirmed
   */
  @javax.annotation.Nullable
  public Boolean getConfirmed() {
    return confirmed;
  }

  public void setConfirmed(Boolean confirmed) {
    this.confirmed = confirmed;
  }


  public CreateOrganizationActionBatchRequest synchronous(Boolean synchronous) {
    this.synchronous = synchronous;
    return this;
  }

  /**
   * Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch. Defaults to false.
   * @return synchronous
   */
  @javax.annotation.Nullable
  public Boolean getSynchronous() {
    return synchronous;
  }

  public void setSynchronous(Boolean synchronous) {
    this.synchronous = synchronous;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateOrganizationActionBatchRequest createOrganizationActionBatchRequest = (CreateOrganizationActionBatchRequest) o;
    return Objects.equals(this.actions, createOrganizationActionBatchRequest.actions) &&
        Objects.equals(this.confirmed, createOrganizationActionBatchRequest.confirmed) &&
        Objects.equals(this.synchronous, createOrganizationActionBatchRequest.synchronous);
  }

  @Override
  public int hashCode() {
    return Objects.hash(actions, confirmed, synchronous);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateOrganizationActionBatchRequest {\n");
    sb.append("    actions: ").append(toIndentedString(actions)).append("\n");
    sb.append("    confirmed: ").append(toIndentedString(confirmed)).append("\n");
    sb.append("    synchronous: ").append(toIndentedString(synchronous)).append("\n");
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
    openapiFields.add("actions");
    openapiFields.add("confirmed");
    openapiFields.add("synchronous");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("actions");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CreateOrganizationActionBatchRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CreateOrganizationActionBatchRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CreateOrganizationActionBatchRequest is not found in the empty JSON string", CreateOrganizationActionBatchRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CreateOrganizationActionBatchRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CreateOrganizationActionBatchRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : CreateOrganizationActionBatchRequest.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the json data is an array
      if (!jsonObj.get("actions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `actions` to be an array in the JSON string but got `%s`", jsonObj.get("actions").toString()));
      }

      JsonArray jsonArrayactions = jsonObj.getAsJsonArray("actions");
      // validate the required field `actions` (array)
      for (int i = 0; i < jsonArrayactions.size(); i++) {
        CreateOrganizationActionBatchRequestActionsInner.validateJsonElement(jsonArrayactions.get(i));
      };
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CreateOrganizationActionBatchRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CreateOrganizationActionBatchRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CreateOrganizationActionBatchRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CreateOrganizationActionBatchRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CreateOrganizationActionBatchRequest>() {
           @Override
           public void write(JsonWriter out, CreateOrganizationActionBatchRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CreateOrganizationActionBatchRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CreateOrganizationActionBatchRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CreateOrganizationActionBatchRequest
   * @throws IOException if the JSON string is invalid with respect to CreateOrganizationActionBatchRequest
   */
  public static CreateOrganizationActionBatchRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CreateOrganizationActionBatchRequest.class);
  }

  /**
   * Convert an instance of CreateOrganizationActionBatchRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

