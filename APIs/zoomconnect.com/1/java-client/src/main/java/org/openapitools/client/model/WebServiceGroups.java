/*
 * www.zoomconnect.com
 * The world's greatest SMS API
 *
 * The version of the OpenAPI document: 1
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
import org.openapitools.client.model.Link;
import org.openapitools.client.model.WebServiceGroup;

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
 * WebServiceGroups
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:22.444535-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class WebServiceGroups {
  public static final String SERIALIZED_NAME_LINKS = "links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<Link> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_WEB_SERVICE_GROUPS = "webServiceGroups";
  @SerializedName(SERIALIZED_NAME_WEB_SERVICE_GROUPS)
  private List<WebServiceGroup> webServiceGroups = new ArrayList<>();

  public WebServiceGroups() {
  }

  public WebServiceGroups links(List<Link> links) {
    this.links = links;
    return this;
  }

  public WebServiceGroups addLinksItem(Link linksItem) {
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
  public List<Link> getLinks() {
    return links;
  }

  public void setLinks(List<Link> links) {
    this.links = links;
  }


  public WebServiceGroups webServiceGroups(List<WebServiceGroup> webServiceGroups) {
    this.webServiceGroups = webServiceGroups;
    return this;
  }

  public WebServiceGroups addWebServiceGroupsItem(WebServiceGroup webServiceGroupsItem) {
    if (this.webServiceGroups == null) {
      this.webServiceGroups = new ArrayList<>();
    }
    this.webServiceGroups.add(webServiceGroupsItem);
    return this;
  }

  /**
   * Get webServiceGroups
   * @return webServiceGroups
   */
  @javax.annotation.Nullable
  public List<WebServiceGroup> getWebServiceGroups() {
    return webServiceGroups;
  }

  public void setWebServiceGroups(List<WebServiceGroup> webServiceGroups) {
    this.webServiceGroups = webServiceGroups;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    WebServiceGroups webServiceGroups = (WebServiceGroups) o;
    return Objects.equals(this.links, webServiceGroups.links) &&
        Objects.equals(this.webServiceGroups, webServiceGroups.webServiceGroups);
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, webServiceGroups);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class WebServiceGroups {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    webServiceGroups: ").append(toIndentedString(webServiceGroups)).append("\n");
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
    openapiFields.add("webServiceGroups");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to WebServiceGroups
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!WebServiceGroups.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in WebServiceGroups is not found in the empty JSON string", WebServiceGroups.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!WebServiceGroups.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `WebServiceGroups` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
            Link.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      if (jsonObj.get("webServiceGroups") != null && !jsonObj.get("webServiceGroups").isJsonNull()) {
        JsonArray jsonArraywebServiceGroups = jsonObj.getAsJsonArray("webServiceGroups");
        if (jsonArraywebServiceGroups != null) {
          // ensure the json data is an array
          if (!jsonObj.get("webServiceGroups").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `webServiceGroups` to be an array in the JSON string but got `%s`", jsonObj.get("webServiceGroups").toString()));
          }

          // validate the optional field `webServiceGroups` (array)
          for (int i = 0; i < jsonArraywebServiceGroups.size(); i++) {
            WebServiceGroup.validateJsonElement(jsonArraywebServiceGroups.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!WebServiceGroups.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'WebServiceGroups' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<WebServiceGroups> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(WebServiceGroups.class));

       return (TypeAdapter<T>) new TypeAdapter<WebServiceGroups>() {
           @Override
           public void write(JsonWriter out, WebServiceGroups value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public WebServiceGroups read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of WebServiceGroups given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of WebServiceGroups
   * @throws IOException if the JSON string is invalid with respect to WebServiceGroups
   */
  public static WebServiceGroups fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, WebServiceGroups.class);
  }

  /**
   * Convert an instance of WebServiceGroups to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

