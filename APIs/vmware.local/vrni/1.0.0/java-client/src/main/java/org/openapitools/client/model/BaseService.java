/*
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.BaseEntity;
import org.openapitools.client.model.EntityType;
import org.openapitools.client.model.PortRange;

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
 * BaseService
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:28.864194-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BaseService extends BaseEntity {
  public static final String SERIALIZED_NAME_PORT_RANGES = "port_ranges";
  @SerializedName(SERIALIZED_NAME_PORT_RANGES)
  private List<PortRange> portRanges = new ArrayList<>();

  public static final String SERIALIZED_NAME_PROTOCOL = "protocol";
  @SerializedName(SERIALIZED_NAME_PROTOCOL)
  private String protocol;

  public BaseService() {
    this.entityType = this.getClass().getSimpleName();
  }

  public BaseService portRanges(List<PortRange> portRanges) {
    this.portRanges = portRanges;
    return this;
  }

  public BaseService addPortRangesItem(PortRange portRangesItem) {
    if (this.portRanges == null) {
      this.portRanges = new ArrayList<>();
    }
    this.portRanges.add(portRangesItem);
    return this;
  }

  /**
   * Get portRanges
   * @return portRanges
   */
  @javax.annotation.Nullable
  public List<PortRange> getPortRanges() {
    return portRanges;
  }

  public void setPortRanges(List<PortRange> portRanges) {
    this.portRanges = portRanges;
  }


  public BaseService protocol(String protocol) {
    this.protocol = protocol;
    return this;
  }

  /**
   * Get protocol
   * @return protocol
   */
  @javax.annotation.Nullable
  public String getProtocol() {
    return protocol;
  }

  public void setProtocol(String protocol) {
    this.protocol = protocol;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BaseService baseService = (BaseService) o;
    return Objects.equals(this.portRanges, baseService.portRanges) &&
        Objects.equals(this.protocol, baseService.protocol) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(portRanges, protocol, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BaseService {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    portRanges: ").append(toIndentedString(portRanges)).append("\n");
    sb.append("    protocol: ").append(toIndentedString(protocol)).append("\n");
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
    openapiFields.add("entity_id");
    openapiFields.add("entity_type");
    openapiFields.add("name");
    openapiFields.add("port_ranges");
    openapiFields.add("protocol");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BaseService
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BaseService.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BaseService is not found in the empty JSON string", BaseService.openapiRequiredFields.toString()));
        }
      }

      String discriminatorValue = jsonElement.getAsJsonObject().get("entity_type").getAsString();
      switch (discriminatorValue) {
        case "EC2Service":
          EC2Service.validateJsonElement(jsonElement);
          break;
        case "NSXService":
          NSXService.validateJsonElement(jsonElement);
          break;
        default:
          throw new IllegalArgumentException(String.format("The value of the `entity_type` field `%s` does not match any key defined in the discriminator's mapping.", discriminatorValue));
      }
  }


  /**
   * Create an instance of BaseService given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BaseService
   * @throws IOException if the JSON string is invalid with respect to BaseService
   */
  public static BaseService fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BaseService.class);
  }

  /**
   * Convert an instance of BaseService to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

