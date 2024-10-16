/*
 * Pendo Feedback API
 * ## Who is this for?  This documentation is for developers creating their own integration with [Feedback's](https://www.pendo.io/product/feedback/) API. If you are doing a standard integration, there's a really easy [Javascript integration](https://help.receptive.io/hc/en-us/articles/209221969-How-to-integrate-Receptive-with-your-app) that you should know about before you go to the effort of building your own integration.  ## Authentication  API calls generally need to be authenticated. Generate an API Key at https://feedback.pendo.io/app/#/vendor/settings?section=integrate. This key should then be added to every request as a request header named 'auth-token' (preferred), or as a query parameter named 'auth-token'.  ## Endpoint  API endpoint is https://api.feedback.eu.pendo.io / https://api.feedback.us.pendo.io depending where your datacenter is located.  ## Notes  API endpoints are being added to this documentation as needed by customers. If you don't see an endpoint you need please contact support and if it exists we'll publish the docs here. The 'try it out' feature on this documentation page will probably be blocked by your browser because the Access-Control-Allow-Origin header has its value set by the Feedback server depending on your hostname.  ## Generating client code  This documentation is automatically generated from an OpenAPI spec available [here](http://apidoc.receptive.io/receptive.swagger.json). You can use Swagger to auto-generate API client code in many languages using the [Swagger Editor](http://editor.swagger.io/#/)
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@receptive.io
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
 * AccountWithTags
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:13.433021-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class AccountWithTags {
  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IS_PAYING = "is_paying";
  @SerializedName(SERIALIZED_NAME_IS_PAYING)
  private Boolean isPaying;

  public static final String SERIALIZED_NAME_MONTHLY_VALUE = "monthly_value";
  @SerializedName(SERIALIZED_NAME_MONTHLY_VALUE)
  private Float monthlyValue;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private String status;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private Object tags;

  public AccountWithTags() {
  }

  public AccountWithTags createdAt(String createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Get createdAt
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(String createdAt) {
    this.createdAt = createdAt;
  }


  public AccountWithTags id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public AccountWithTags isPaying(Boolean isPaying) {
    this.isPaying = isPaying;
    return this;
  }

  /**
   * Get isPaying
   * @return isPaying
   */
  @javax.annotation.Nullable
  public Boolean getIsPaying() {
    return isPaying;
  }

  public void setIsPaying(Boolean isPaying) {
    this.isPaying = isPaying;
  }


  public AccountWithTags monthlyValue(Float monthlyValue) {
    this.monthlyValue = monthlyValue;
    return this;
  }

  /**
   * Get monthlyValue
   * @return monthlyValue
   */
  @javax.annotation.Nullable
  public Float getMonthlyValue() {
    return monthlyValue;
  }

  public void setMonthlyValue(Float monthlyValue) {
    this.monthlyValue = monthlyValue;
  }


  public AccountWithTags name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public AccountWithTags status(String status) {
    this.status = status;
    return this;
  }

  /**
   * Get status
   * @return status
   */
  @javax.annotation.Nullable
  public String getStatus() {
    return status;
  }

  public void setStatus(String status) {
    this.status = status;
  }


  public AccountWithTags tags(Object tags) {
    this.tags = tags;
    return this;
  }

  /**
   * Tags can contain simple tags or categorised tags. Simple tags are supplied as an array of Strings Simple Tag Example: [&#39;Foo&#39;, &#39;Bar&#39;].  To put the tags in categories replace the Strings with maps of using tag category as the key and tag value as the value where value can be array of strings, e.g Categorised Tag Example: [ {&#39;Color&#39;:[&#39;Red&#39;, &#39;Yellow&#39;]},  {&#39;Flavor&#39;:[&#39;Cherry&#39;]} ]  Simple and categorised tags can be mixed in the same array. Below validations are done on the tag values of both simple and categorised tags: 1. Tag values must be strings 2. Tags must be at least 2 characters in length 3. Invalid characters (we dont accept following characters in tag value)  , | { } : &lt; &gt; 
   * @return tags
   */
  @javax.annotation.Nullable
  public Object getTags() {
    return tags;
  }

  public void setTags(Object tags) {
    this.tags = tags;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AccountWithTags accountWithTags = (AccountWithTags) o;
    return Objects.equals(this.createdAt, accountWithTags.createdAt) &&
        Objects.equals(this.id, accountWithTags.id) &&
        Objects.equals(this.isPaying, accountWithTags.isPaying) &&
        Objects.equals(this.monthlyValue, accountWithTags.monthlyValue) &&
        Objects.equals(this.name, accountWithTags.name) &&
        Objects.equals(this.status, accountWithTags.status) &&
        Objects.equals(this.tags, accountWithTags.tags);
  }

  @Override
  public int hashCode() {
    return Objects.hash(createdAt, id, isPaying, monthlyValue, name, status, tags);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AccountWithTags {\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isPaying: ").append(toIndentedString(isPaying)).append("\n");
    sb.append("    monthlyValue: ").append(toIndentedString(monthlyValue)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
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
    openapiFields.add("created_at");
    openapiFields.add("id");
    openapiFields.add("is_paying");
    openapiFields.add("monthly_value");
    openapiFields.add("name");
    openapiFields.add("status");
    openapiFields.add("tags");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to AccountWithTags
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!AccountWithTags.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in AccountWithTags is not found in the empty JSON string", AccountWithTags.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!AccountWithTags.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `AccountWithTags` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) && !jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!AccountWithTags.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'AccountWithTags' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<AccountWithTags> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(AccountWithTags.class));

       return (TypeAdapter<T>) new TypeAdapter<AccountWithTags>() {
           @Override
           public void write(JsonWriter out, AccountWithTags value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public AccountWithTags read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of AccountWithTags given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of AccountWithTags
   * @throws IOException if the JSON string is invalid with respect to AccountWithTags
   */
  public static AccountWithTags fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, AccountWithTags.class);
  }

  /**
   * Convert an instance of AccountWithTags to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

