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
import org.openapitools.client.model.WebServiceMessage;

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
 * WebServiceMessages
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:12:22.444535-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class WebServiceMessages {
  public static final String SERIALIZED_NAME_ELEMENTS = "elements";
  @SerializedName(SERIALIZED_NAME_ELEMENTS)
  private Integer elements;

  public static final String SERIALIZED_NAME_LINKS = "links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<Link> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_PAGE = "page";
  @SerializedName(SERIALIZED_NAME_PAGE)
  private Integer page;

  public static final String SERIALIZED_NAME_PAGE_SIZE = "pageSize";
  @SerializedName(SERIALIZED_NAME_PAGE_SIZE)
  private Integer pageSize;

  public static final String SERIALIZED_NAME_TOTAL_ELEMENTS = "totalElements";
  @SerializedName(SERIALIZED_NAME_TOTAL_ELEMENTS)
  private Long totalElements;

  public static final String SERIALIZED_NAME_TOTAL_PAGES = "totalPages";
  @SerializedName(SERIALIZED_NAME_TOTAL_PAGES)
  private Integer totalPages;

  public static final String SERIALIZED_NAME_WEB_SERVICE_MESSAGES = "webServiceMessages";
  @SerializedName(SERIALIZED_NAME_WEB_SERVICE_MESSAGES)
  private List<WebServiceMessage> webServiceMessages = new ArrayList<>();

  public WebServiceMessages() {
  }

  public WebServiceMessages elements(Integer elements) {
    this.elements = elements;
    return this;
  }

  /**
   * Get elements
   * @return elements
   */
  @javax.annotation.Nullable
  public Integer getElements() {
    return elements;
  }

  public void setElements(Integer elements) {
    this.elements = elements;
  }


  public WebServiceMessages links(List<Link> links) {
    this.links = links;
    return this;
  }

  public WebServiceMessages addLinksItem(Link linksItem) {
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


  public WebServiceMessages page(Integer page) {
    this.page = page;
    return this;
  }

  /**
   * Get page
   * @return page
   */
  @javax.annotation.Nullable
  public Integer getPage() {
    return page;
  }

  public void setPage(Integer page) {
    this.page = page;
  }


  public WebServiceMessages pageSize(Integer pageSize) {
    this.pageSize = pageSize;
    return this;
  }

  /**
   * Get pageSize
   * @return pageSize
   */
  @javax.annotation.Nullable
  public Integer getPageSize() {
    return pageSize;
  }

  public void setPageSize(Integer pageSize) {
    this.pageSize = pageSize;
  }


  public WebServiceMessages totalElements(Long totalElements) {
    this.totalElements = totalElements;
    return this;
  }

  /**
   * Get totalElements
   * @return totalElements
   */
  @javax.annotation.Nullable
  public Long getTotalElements() {
    return totalElements;
  }

  public void setTotalElements(Long totalElements) {
    this.totalElements = totalElements;
  }


  public WebServiceMessages totalPages(Integer totalPages) {
    this.totalPages = totalPages;
    return this;
  }

  /**
   * Get totalPages
   * @return totalPages
   */
  @javax.annotation.Nullable
  public Integer getTotalPages() {
    return totalPages;
  }

  public void setTotalPages(Integer totalPages) {
    this.totalPages = totalPages;
  }


  public WebServiceMessages webServiceMessages(List<WebServiceMessage> webServiceMessages) {
    this.webServiceMessages = webServiceMessages;
    return this;
  }

  public WebServiceMessages addWebServiceMessagesItem(WebServiceMessage webServiceMessagesItem) {
    if (this.webServiceMessages == null) {
      this.webServiceMessages = new ArrayList<>();
    }
    this.webServiceMessages.add(webServiceMessagesItem);
    return this;
  }

  /**
   * Get webServiceMessages
   * @return webServiceMessages
   */
  @javax.annotation.Nullable
  public List<WebServiceMessage> getWebServiceMessages() {
    return webServiceMessages;
  }

  public void setWebServiceMessages(List<WebServiceMessage> webServiceMessages) {
    this.webServiceMessages = webServiceMessages;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    WebServiceMessages webServiceMessages = (WebServiceMessages) o;
    return Objects.equals(this.elements, webServiceMessages.elements) &&
        Objects.equals(this.links, webServiceMessages.links) &&
        Objects.equals(this.page, webServiceMessages.page) &&
        Objects.equals(this.pageSize, webServiceMessages.pageSize) &&
        Objects.equals(this.totalElements, webServiceMessages.totalElements) &&
        Objects.equals(this.totalPages, webServiceMessages.totalPages) &&
        Objects.equals(this.webServiceMessages, webServiceMessages.webServiceMessages);
  }

  @Override
  public int hashCode() {
    return Objects.hash(elements, links, page, pageSize, totalElements, totalPages, webServiceMessages);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class WebServiceMessages {\n");
    sb.append("    elements: ").append(toIndentedString(elements)).append("\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    page: ").append(toIndentedString(page)).append("\n");
    sb.append("    pageSize: ").append(toIndentedString(pageSize)).append("\n");
    sb.append("    totalElements: ").append(toIndentedString(totalElements)).append("\n");
    sb.append("    totalPages: ").append(toIndentedString(totalPages)).append("\n");
    sb.append("    webServiceMessages: ").append(toIndentedString(webServiceMessages)).append("\n");
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
    openapiFields.add("elements");
    openapiFields.add("links");
    openapiFields.add("page");
    openapiFields.add("pageSize");
    openapiFields.add("totalElements");
    openapiFields.add("totalPages");
    openapiFields.add("webServiceMessages");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to WebServiceMessages
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!WebServiceMessages.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in WebServiceMessages is not found in the empty JSON string", WebServiceMessages.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!WebServiceMessages.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `WebServiceMessages` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
      if (jsonObj.get("webServiceMessages") != null && !jsonObj.get("webServiceMessages").isJsonNull()) {
        JsonArray jsonArraywebServiceMessages = jsonObj.getAsJsonArray("webServiceMessages");
        if (jsonArraywebServiceMessages != null) {
          // ensure the json data is an array
          if (!jsonObj.get("webServiceMessages").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `webServiceMessages` to be an array in the JSON string but got `%s`", jsonObj.get("webServiceMessages").toString()));
          }

          // validate the optional field `webServiceMessages` (array)
          for (int i = 0; i < jsonArraywebServiceMessages.size(); i++) {
            WebServiceMessage.validateJsonElement(jsonArraywebServiceMessages.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!WebServiceMessages.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'WebServiceMessages' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<WebServiceMessages> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(WebServiceMessages.class));

       return (TypeAdapter<T>) new TypeAdapter<WebServiceMessages>() {
           @Override
           public void write(JsonWriter out, WebServiceMessages value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public WebServiceMessages read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of WebServiceMessages given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of WebServiceMessages
   * @throws IOException if the JSON string is invalid with respect to WebServiceMessages
   */
  public static WebServiceMessages fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, WebServiceMessages.class);
  }

  /**
   * Convert an instance of WebServiceMessages to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

