/*
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
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
import org.openapitools.client.model.Href;

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
 * NavigatorExtension describes the Navigator extension point in the UI
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:51.881749-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class NavigatorExtension {
  public static final String SERIALIZED_NAME_CHILDREN = "children";
  @SerializedName(SERIALIZED_NAME_CHILDREN)
  private List<NavigatorExtension> children = new ArrayList<>();

  public static final String SERIALIZED_NAME_COMPONENT = "component";
  @SerializedName(SERIALIZED_NAME_COMPONENT)
  private String component;

  public static final String SERIALIZED_NAME_HREF = "href";
  @SerializedName(SERIALIZED_NAME_HREF)
  private Href href;

  public static final String SERIALIZED_NAME_ICON = "icon";
  @SerializedName(SERIALIZED_NAME_ICON)
  private String icon;

  public static final String SERIALIZED_NAME_LINK = "link";
  @SerializedName(SERIALIZED_NAME_LINK)
  private Boolean link;

  public static final String SERIALIZED_NAME_SHOW = "show";
  @SerializedName(SERIALIZED_NAME_SHOW)
  private Boolean show;

  public static final String SERIALIZED_NAME_TITLE = "title";
  @SerializedName(SERIALIZED_NAME_TITLE)
  private String title;

  public NavigatorExtension() {
  }

  public NavigatorExtension children(List<NavigatorExtension> children) {
    this.children = children;
    return this;
  }

  public NavigatorExtension addChildrenItem(NavigatorExtension childrenItem) {
    if (this.children == null) {
      this.children = new ArrayList<>();
    }
    this.children.add(childrenItem);
    return this;
  }

  /**
   * NavigatorExtensions is a collection of NavigatorExtension
   * @return children
   */
  @javax.annotation.Nullable
  public List<NavigatorExtension> getChildren() {
    return children;
  }

  public void setChildren(List<NavigatorExtension> children) {
    this.children = children;
  }


  public NavigatorExtension component(String component) {
    this.component = component;
    return this;
  }

  /**
   * Get component
   * @return component
   */
  @javax.annotation.Nullable
  public String getComponent() {
    return component;
  }

  public void setComponent(String component) {
    this.component = component;
  }


  public NavigatorExtension href(Href href) {
    this.href = href;
    return this;
  }

  /**
   * Get href
   * @return href
   */
  @javax.annotation.Nullable
  public Href getHref() {
    return href;
  }

  public void setHref(Href href) {
    this.href = href;
  }


  public NavigatorExtension icon(String icon) {
    this.icon = icon;
    return this;
  }

  /**
   * Get icon
   * @return icon
   */
  @javax.annotation.Nullable
  public String getIcon() {
    return icon;
  }

  public void setIcon(String icon) {
    this.icon = icon;
  }


  public NavigatorExtension link(Boolean link) {
    this.link = link;
    return this;
  }

  /**
   * Get link
   * @return link
   */
  @javax.annotation.Nullable
  public Boolean getLink() {
    return link;
  }

  public void setLink(Boolean link) {
    this.link = link;
  }


  public NavigatorExtension show(Boolean show) {
    this.show = show;
    return this;
  }

  /**
   * Get show
   * @return show
   */
  @javax.annotation.Nullable
  public Boolean getShow() {
    return show;
  }

  public void setShow(Boolean show) {
    this.show = show;
  }


  public NavigatorExtension title(String title) {
    this.title = title;
    return this;
  }

  /**
   * Get title
   * @return title
   */
  @javax.annotation.Nullable
  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    NavigatorExtension navigatorExtension = (NavigatorExtension) o;
    return Objects.equals(this.children, navigatorExtension.children) &&
        Objects.equals(this.component, navigatorExtension.component) &&
        Objects.equals(this.href, navigatorExtension.href) &&
        Objects.equals(this.icon, navigatorExtension.icon) &&
        Objects.equals(this.link, navigatorExtension.link) &&
        Objects.equals(this.show, navigatorExtension.show) &&
        Objects.equals(this.title, navigatorExtension.title);
  }

  @Override
  public int hashCode() {
    return Objects.hash(children, component, href, icon, link, show, title);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class NavigatorExtension {\n");
    sb.append("    children: ").append(toIndentedString(children)).append("\n");
    sb.append("    component: ").append(toIndentedString(component)).append("\n");
    sb.append("    href: ").append(toIndentedString(href)).append("\n");
    sb.append("    icon: ").append(toIndentedString(icon)).append("\n");
    sb.append("    link: ").append(toIndentedString(link)).append("\n");
    sb.append("    show: ").append(toIndentedString(show)).append("\n");
    sb.append("    title: ").append(toIndentedString(title)).append("\n");
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
    openapiFields.add("children");
    openapiFields.add("component");
    openapiFields.add("href");
    openapiFields.add("icon");
    openapiFields.add("link");
    openapiFields.add("show");
    openapiFields.add("title");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to NavigatorExtension
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!NavigatorExtension.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in NavigatorExtension is not found in the empty JSON string", NavigatorExtension.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!NavigatorExtension.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `NavigatorExtension` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("children") != null && !jsonObj.get("children").isJsonNull()) {
        JsonArray jsonArraychildren = jsonObj.getAsJsonArray("children");
        if (jsonArraychildren != null) {
          // ensure the json data is an array
          if (!jsonObj.get("children").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `children` to be an array in the JSON string but got `%s`", jsonObj.get("children").toString()));
          }

          // validate the optional field `children` (array)
          for (int i = 0; i < jsonArraychildren.size(); i++) {
            NavigatorExtension.validateJsonElement(jsonArraychildren.get(i));
          };
        }
      }
      if ((jsonObj.get("component") != null && !jsonObj.get("component").isJsonNull()) && !jsonObj.get("component").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `component` to be a primitive type in the JSON string but got `%s`", jsonObj.get("component").toString()));
      }
      // validate the optional field `href`
      if (jsonObj.get("href") != null && !jsonObj.get("href").isJsonNull()) {
        Href.validateJsonElement(jsonObj.get("href"));
      }
      if ((jsonObj.get("icon") != null && !jsonObj.get("icon").isJsonNull()) && !jsonObj.get("icon").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `icon` to be a primitive type in the JSON string but got `%s`", jsonObj.get("icon").toString()));
      }
      if ((jsonObj.get("title") != null && !jsonObj.get("title").isJsonNull()) && !jsonObj.get("title").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `title` to be a primitive type in the JSON string but got `%s`", jsonObj.get("title").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!NavigatorExtension.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'NavigatorExtension' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<NavigatorExtension> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(NavigatorExtension.class));

       return (TypeAdapter<T>) new TypeAdapter<NavigatorExtension>() {
           @Override
           public void write(JsonWriter out, NavigatorExtension value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public NavigatorExtension read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of NavigatorExtension given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of NavigatorExtension
   * @throws IOException if the JSON string is invalid with respect to NavigatorExtension
   */
  public static NavigatorExtension fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, NavigatorExtension.class);
  }

  /**
   * Convert an instance of NavigatorExtension to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

