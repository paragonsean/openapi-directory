/*
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
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
import org.openapitools.client.model.FileLinksInner;

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
 * ModelFile
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T11:20:59.825309-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ModelFile {
  public static final String SERIALIZED_NAME_LINKS = "_links";
  @SerializedName(SERIALIZED_NAME_LINKS)
  private List<FileLinksInner> links = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREATED_TIME = "createdTime";
  @SerializedName(SERIALIZED_NAME_CREATED_TIME)
  private OffsetDateTime createdTime;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_EXTENSION = "extension";
  @SerializedName(SERIALIZED_NAME_EXTENSION)
  private String extension;

  public static final String SERIALIZED_NAME_HEIGHT = "height";
  @SerializedName(SERIALIZED_NAME_HEIGHT)
  private Integer height;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_IS_PUBLIC = "isPublic";
  @SerializedName(SERIALIZED_NAME_IS_PUBLIC)
  private Boolean isPublic;

  /**
   * The mime type.
   */
  @JsonAdapter(MimeEnum.Adapter.class)
  public enum MimeEnum {
    IMAGE_PNG("image/png"),
    
    IMAGE_JPEG("image/jpeg"),
    
    IMAGE_GIF("image/gif"),
    
    APPLICATION_PDF("application/pdf"),
    
    AUDIO_MPEG("audio/mpeg");

    private String value;

    MimeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static MimeEnum fromValue(String value) {
      for (MimeEnum b : MimeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<MimeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final MimeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public MimeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return MimeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      MimeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_MIME = "mime";
  @SerializedName(SERIALIZED_NAME_MIME)
  private MimeEnum mime;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_SHA1 = "sha1";
  @SerializedName(SERIALIZED_NAME_SHA1)
  private String sha1;

  public static final String SERIALIZED_NAME_SIZE = "size";
  @SerializedName(SERIALIZED_NAME_SIZE)
  private Integer size;

  public static final String SERIALIZED_NAME_TAGS = "tags";
  @SerializedName(SERIALIZED_NAME_TAGS)
  private List<String> tags = new ArrayList<>();

  public static final String SERIALIZED_NAME_UPDATED_TIME = "updatedTime";
  @SerializedName(SERIALIZED_NAME_UPDATED_TIME)
  private OffsetDateTime updatedTime;

  public static final String SERIALIZED_NAME_WIDTH = "width";
  @SerializedName(SERIALIZED_NAME_WIDTH)
  private Integer width;

  public ModelFile() {
  }

  public ModelFile(
     List<FileLinksInner> links, 
     OffsetDateTime createdTime, 
     Integer height, 
     String id, 
     MimeEnum mime, 
     String sha1, 
     Integer size, 
     OffsetDateTime updatedTime, 
     Integer width
  ) {
    this();
    this.links = links;
    this.createdTime = createdTime;
    this.height = height;
    this.id = id;
    this.mime = mime;
    this.sha1 = sha1;
    this.size = size;
    this.updatedTime = updatedTime;
    this.width = width;
  }

  /**
   * The links related to resource.
   * @return links
   */
  @javax.annotation.Nullable
  public List<FileLinksInner> getLinks() {
    return links;
  }



  /**
   * The upload date/time.
   * @return createdTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getCreatedTime() {
    return createdTime;
  }



  public ModelFile description(String description) {
    this.description = description;
    return this;
  }

  /**
   * The File description.
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public ModelFile extension(String extension) {
    this.extension = extension;
    return this;
  }

  /**
   * The File extension.
   * @return extension
   */
  @javax.annotation.Nullable
  public String getExtension() {
    return extension;
  }

  public void setExtension(String extension) {
    this.extension = extension;
  }


  /**
   * Image height, applicable to images only.
   * @return height
   */
  @javax.annotation.Nullable
  public Integer getHeight() {
    return height;
  }



  /**
   * The resource ID. Defaults to UUID v4.
   * @return id
   */
  @javax.annotation.Nullable
  public String getId() {
    return id;
  }



  public ModelFile isPublic(Boolean isPublic) {
    this.isPublic = isPublic;
    return this;
  }

  /**
   * Is the file available publicly (without authentication). If true, the permalink in the _links section contains the public URL.
   * @return isPublic
   */
  @javax.annotation.Nullable
  public Boolean getIsPublic() {
    return isPublic;
  }

  public void setIsPublic(Boolean isPublic) {
    this.isPublic = isPublic;
  }


  /**
   * The mime type.
   * @return mime
   */
  @javax.annotation.Nullable
  public MimeEnum getMime() {
    return mime;
  }



  public ModelFile name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Original File name.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  /**
   * Hash sum of the file.
   * @return sha1
   */
  @javax.annotation.Nullable
  public String getSha1() {
    return sha1;
  }



  /**
   * The File size in bytes.
   * @return size
   */
  @javax.annotation.Nullable
  public Integer getSize() {
    return size;
  }



  public ModelFile tags(List<String> tags) {
    this.tags = tags;
    return this;
  }

  public ModelFile addTagsItem(String tagsItem) {
    if (this.tags == null) {
      this.tags = new ArrayList<>();
    }
    this.tags.add(tagsItem);
    return this;
  }

  /**
   * The tags list.
   * @return tags
   */
  @javax.annotation.Nullable
  public List<String> getTags() {
    return tags;
  }

  public void setTags(List<String> tags) {
    this.tags = tags;
  }


  /**
   * The latest update date/time.
   * @return updatedTime
   */
  @javax.annotation.Nullable
  public OffsetDateTime getUpdatedTime() {
    return updatedTime;
  }



  /**
   * Image width, applicable to images only.
   * @return width
   */
  @javax.annotation.Nullable
  public Integer getWidth() {
    return width;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ModelFile _file = (ModelFile) o;
    return Objects.equals(this.links, _file.links) &&
        Objects.equals(this.createdTime, _file.createdTime) &&
        Objects.equals(this.description, _file.description) &&
        Objects.equals(this.extension, _file.extension) &&
        Objects.equals(this.height, _file.height) &&
        Objects.equals(this.id, _file.id) &&
        Objects.equals(this.isPublic, _file.isPublic) &&
        Objects.equals(this.mime, _file.mime) &&
        Objects.equals(this.name, _file.name) &&
        Objects.equals(this.sha1, _file.sha1) &&
        Objects.equals(this.size, _file.size) &&
        Objects.equals(this.tags, _file.tags) &&
        Objects.equals(this.updatedTime, _file.updatedTime) &&
        Objects.equals(this.width, _file.width);
  }

  @Override
  public int hashCode() {
    return Objects.hash(links, createdTime, description, extension, height, id, isPublic, mime, name, sha1, size, tags, updatedTime, width);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ModelFile {\n");
    sb.append("    links: ").append(toIndentedString(links)).append("\n");
    sb.append("    createdTime: ").append(toIndentedString(createdTime)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    extension: ").append(toIndentedString(extension)).append("\n");
    sb.append("    height: ").append(toIndentedString(height)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isPublic: ").append(toIndentedString(isPublic)).append("\n");
    sb.append("    mime: ").append(toIndentedString(mime)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    sha1: ").append(toIndentedString(sha1)).append("\n");
    sb.append("    size: ").append(toIndentedString(size)).append("\n");
    sb.append("    tags: ").append(toIndentedString(tags)).append("\n");
    sb.append("    updatedTime: ").append(toIndentedString(updatedTime)).append("\n");
    sb.append("    width: ").append(toIndentedString(width)).append("\n");
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
    openapiFields.add("_links");
    openapiFields.add("createdTime");
    openapiFields.add("description");
    openapiFields.add("extension");
    openapiFields.add("height");
    openapiFields.add("id");
    openapiFields.add("isPublic");
    openapiFields.add("mime");
    openapiFields.add("name");
    openapiFields.add("sha1");
    openapiFields.add("size");
    openapiFields.add("tags");
    openapiFields.add("updatedTime");
    openapiFields.add("width");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ModelFile
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ModelFile.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ModelFile is not found in the empty JSON string", ModelFile.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ModelFile.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ModelFile` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("_links") != null && !jsonObj.get("_links").isJsonNull()) {
        JsonArray jsonArraylinks = jsonObj.getAsJsonArray("_links");
        if (jsonArraylinks != null) {
          // ensure the json data is an array
          if (!jsonObj.get("_links").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `_links` to be an array in the JSON string but got `%s`", jsonObj.get("_links").toString()));
          }

          // validate the optional field `_links` (array)
          for (int i = 0; i < jsonArraylinks.size(); i++) {
            FileLinksInner.validateJsonElement(jsonArraylinks.get(i));
          };
        }
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("extension") != null && !jsonObj.get("extension").isJsonNull()) && !jsonObj.get("extension").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `extension` to be a primitive type in the JSON string but got `%s`", jsonObj.get("extension").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("mime") != null && !jsonObj.get("mime").isJsonNull()) && !jsonObj.get("mime").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mime` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mime").toString()));
      }
      // validate the optional field `mime`
      if (jsonObj.get("mime") != null && !jsonObj.get("mime").isJsonNull()) {
        MimeEnum.validateJsonElement(jsonObj.get("mime"));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("sha1") != null && !jsonObj.get("sha1").isJsonNull()) && !jsonObj.get("sha1").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sha1` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sha1").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("tags") != null && !jsonObj.get("tags").isJsonNull() && !jsonObj.get("tags").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tags` to be an array in the JSON string but got `%s`", jsonObj.get("tags").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ModelFile.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ModelFile' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ModelFile> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ModelFile.class));

       return (TypeAdapter<T>) new TypeAdapter<ModelFile>() {
           @Override
           public void write(JsonWriter out, ModelFile value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ModelFile read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ModelFile given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ModelFile
   * @throws IOException if the JSON string is invalid with respect to ModelFile
   */
  public static ModelFile fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ModelFile.class);
  }

  /**
   * Convert an instance of ModelFile to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

