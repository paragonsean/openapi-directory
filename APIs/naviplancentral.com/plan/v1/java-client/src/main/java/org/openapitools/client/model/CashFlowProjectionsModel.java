/*
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
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
import org.openapitools.client.model.CashFlowProjectionModel;
import org.openapitools.client.model.ObjectLink;

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
 * CashFlowProjectionsModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:57:21.776546-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CashFlowProjectionsModel {
  public static final String SERIALIZED_NAME_LINKS = "links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<ObjectLink> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_PROJECTIONS = "projections";
  @SerializedName(SERIALIZED_NAME_PROJECTIONS)
  private List<CashFlowProjectionModel> projections = new ArrayList<>();

  public CashFlowProjectionsModel() {
  }

  public CashFlowProjectionsModel links(List<ObjectLink> links) {
    this.links = links;
    return this;
  }

  public CashFlowProjectionsModel addLinksItem(ObjectLink linksItem) {
    if (this.links == null) {
      this.links = new ArrayList<>();
    }
    this.links.add(linksItem);
    return this;
  }

  /**
   * Get links
   * @return links
   */
  @javax.annotation.Nullable
  public List<ObjectLink> getLinks() {
    return links;
  }

  public void setLinks(List<ObjectLink> links) {
    this.links = links;
  }


  public CashFlowProjectionsModel projections(List<CashFlowProjectionModel> projections) {
    this.projections = projections;
    return this;
  }

  public CashFlowProjectionsModel addProjectionsItem(CashFlowProjectionModel projectionsItem) {
    if (this.projections == null) {
      this.projections = new ArrayList<>();
    }
    this.projections.add(projectionsItem);
    return this;
  }

  /**
   * Get projections
   * @return projections
   */
  @javax.annotation.Nullable
  public List<CashFlowProjectionModel> getProjections() {
    return projections;
  }

  public void setProjections(List<CashFlowProjectionModel> projections) {
    this.projections = projections;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CashFlowProjectionsModel cashFlowProjectionsModel = (CashFlowProjectionsModel) o;
    return Objects.equals(this.links, cashFlowProjectionsModel.links) &&
        Objects.equals(this.projections, cashFlowProjectionsModel.projections);
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, projections);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CashFlowProjectionsModel {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    projections: ").append(toIndentedString(projections)).append("\n");
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
    openapiFields.add("links");
    openapiFields.add("projections");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CashFlowProjectionsModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CashFlowProjectionsModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CashFlowProjectionsModel is not found in the empty JSON string", CashFlowProjectionsModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CashFlowProjectionsModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CashFlowProjectionsModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("links") != null && !jsonObj.get("links").isJsonNull()) {
        JsonArray jsonArraylinks = jsonObj.getAsJsonArray("links");
        if (jsonArraylinks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("links").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `links` to be an array in the JSON string but got `%s`", jsonObj.get("links").toString()));
          }

          // validate the optional field `links` (array)
          for (int i = 0; i < jsonArraylinks.size(); i++) {
            ObjectLink.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      if (jsonObj.get("projections") != null && !jsonObj.get("projections").isJsonNull()) {
        JsonArray jsonArrayprojections = jsonObj.getAsJsonArray("projections");
        if (jsonArrayprojections != null) {
          // ensure the json data is an array
          if (!jsonObj.get("projections").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `projections` to be an array in the JSON string but got `%s`", jsonObj.get("projections").toString()));
          }

          // validate the optional field `projections` (array)
          for (int i = 0; i < jsonArrayprojections.size(); i++) {
            CashFlowProjectionModel.validateJsonElement(jsonArrayprojections.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CashFlowProjectionsModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CashFlowProjectionsModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CashFlowProjectionsModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CashFlowProjectionsModel.class));

       return (TypeAdapter<T>) new TypeAdapter<CashFlowProjectionsModel>() {
           @Override
           public void write(JsonWriter out, CashFlowProjectionsModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CashFlowProjectionsModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CashFlowProjectionsModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CashFlowProjectionsModel
   * @throws IOException if the JSON string is invalid with respect to CashFlowProjectionsModel
   */
  public static CashFlowProjectionsModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CashFlowProjectionsModel.class);
  }

  /**
   * Convert an instance of CashFlowProjectionsModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

