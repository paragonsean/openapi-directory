/*
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
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
 * Network access control entry.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:24:47.141391-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner {
  /**
   * Action object.
   */
  @JsonAdapter(ActionEnum.Adapter.class)
  public enum ActionEnum {
    PERMIT("Permit"),
    
    DENY("Deny");

    private String value;

    ActionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ActionEnum fromValue(String value) {
      for (ActionEnum b : ActionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ActionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ActionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ActionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ActionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ActionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_ACTION = "action";
  @SerializedName(SERIALIZED_NAME_ACTION)
  private ActionEnum action;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ORDER = "order";
  @SerializedName(SERIALIZED_NAME_ORDER)
  private Integer order;

  public static final String SERIALIZED_NAME_REMOTE_SUBNET = "remoteSubnet";
  @SerializedName(SERIALIZED_NAME_REMOTE_SUBNET)
  private String remoteSubnet;

  public DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner() {
  }

  public DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner action(ActionEnum action) {
    this.action = action;
    return this;
  }

  /**
   * Action object.
   * @return action
   */
  @javax.annotation.Nullable
  public ActionEnum getAction() {
    return action;
  }

  public void setAction(ActionEnum action) {
    this.action = action;
  }


  public DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Description of network access control entry.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner order(Integer order) {
    this.order = order;
    return this;
  }

  /**
   * Order of precedence.
   * @return order
   */
  @javax.annotation.Nullable
  public Integer getOrder() {
    return order;
  }

  public void setOrder(Integer order) {
    this.order = order;
  }


  public DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner remoteSubnet(String remoteSubnet) {
    this.remoteSubnet = remoteSubnet;
    return this;
  }

  /**
   * Remote subnet.
   * @return remoteSubnet
   */
  @javax.annotation.Nullable
  public String getRemoteSubnet() {
    return remoteSubnet;
  }

  public void setRemoteSubnet(String remoteSubnet) {
    this.remoteSubnet = remoteSubnet;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner deploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner = (DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner) o;
    return Objects.equals(this.action, deploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner.action) &&
        Objects.equals(this.description, deploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner.description) &&
        Objects.equals(this.order, deploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner.order) &&
        Objects.equals(this.remoteSubnet, deploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner.remoteSubnet);
  }

  @Override
  public int hashCode() {
    return Objects.hash(action, description, order, remoteSubnet);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner {\n");
    sb.append("    action: ").append(toIndentedString(action)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    order: ").append(toIndentedString(order)).append("\n");
    sb.append("    remoteSubnet: ").append(toIndentedString(remoteSubnet)).append("\n");
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
    openapiFields.add("action");
    openapiFields.add("description");
    openapiFields.add("order");
    openapiFields.add("remoteSubnet");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner is not found in the empty JSON string", DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("action") != null && !jsonObj.get("action").isJsonNull()) && !jsonObj.get("action").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `action` to be a primitive type in the JSON string but got `%s`", jsonObj.get("action").toString()));
      }
      // validate the optional field `action`
      if (jsonObj.get("action") != null && !jsonObj.get("action").isJsonNull()) {
        ActionEnum.validateJsonElement(jsonObj.get("action"));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("remoteSubnet") != null && !jsonObj.get("remoteSubnet").isJsonNull()) && !jsonObj.get("remoteSubnet").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `remoteSubnet` to be a primitive type in the JSON string but got `%s`", jsonObj.get("remoteSubnet").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner.class));

       return (TypeAdapter<T>) new TypeAdapter<DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner>() {
           @Override
           public void write(JsonWriter out, DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner
   * @throws IOException if the JSON string is invalid with respect to DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner
   */
  public static DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner.class);
  }

  /**
   * Convert an instance of DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

