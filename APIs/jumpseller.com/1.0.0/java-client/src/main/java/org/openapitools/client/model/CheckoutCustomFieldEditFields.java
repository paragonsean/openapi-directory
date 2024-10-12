/*
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
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
 * CheckoutCustomFieldEditFields
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:37.537066-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CheckoutCustomFieldEditFields {
  /**
   * Area of the CheckoutCustomField
   */
  @JsonAdapter(AreaEnum.Adapter.class)
  public enum AreaEnum {
    CONTACT("contact"),
    
    BILLING_SHIPPING("billing_shipping"),
    
    OTHER("other");

    private String value;

    AreaEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static AreaEnum fromValue(String value) {
      for (AreaEnum b : AreaEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<AreaEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final AreaEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public AreaEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return AreaEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      AreaEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_AREA = "area";
  @SerializedName(SERIALIZED_NAME_AREA)
  private AreaEnum area;

  public static final String SERIALIZED_NAME_CUSTOM_FIELD_SELECT_OPTIONS = "custom_field_select_options";
  @SerializedName(SERIALIZED_NAME_CUSTOM_FIELD_SELECT_OPTIONS)
  private List<String> customFieldSelectOptions = new ArrayList<>();

  public static final String SERIALIZED_NAME_DELETABLE = "deletable";
  @SerializedName(SERIALIZED_NAME_DELETABLE)
  private Boolean deletable = false;

  public static final String SERIALIZED_NAME_LABEL = "label";
  @SerializedName(SERIALIZED_NAME_LABEL)
  private String label;

  public static final String SERIALIZED_NAME_POSITION = "position";
  @SerializedName(SERIALIZED_NAME_POSITION)
  private Integer position;

  public static final String SERIALIZED_NAME_REQUIRED = "required";
  @SerializedName(SERIALIZED_NAME_REQUIRED)
  private Boolean required = false;

  /**
   * Type of the CheckoutCustomField
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    TEXT("text"),
    
    SELECT("select"),
    
    INPUT("input"),
    
    CHECKBOX("checkbox"),
    
    DATE("date");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type;

  public CheckoutCustomFieldEditFields() {
  }

  public CheckoutCustomFieldEditFields area(AreaEnum area) {
    this.area = area;
    return this;
  }

  /**
   * Area of the CheckoutCustomField
   * @return area
   */
  @javax.annotation.Nullable
  public AreaEnum getArea() {
    return area;
  }

  public void setArea(AreaEnum area) {
    this.area = area;
  }


  public CheckoutCustomFieldEditFields customFieldSelectOptions(List<String> customFieldSelectOptions) {
    this.customFieldSelectOptions = customFieldSelectOptions;
    return this;
  }

  public CheckoutCustomFieldEditFields addCustomFieldSelectOptionsItem(String customFieldSelectOptionsItem) {
    if (this.customFieldSelectOptions == null) {
      this.customFieldSelectOptions = new ArrayList<>();
    }
    this.customFieldSelectOptions.add(customFieldSelectOptionsItem);
    return this;
  }

  /**
   * The values for the CheckoutCustomField selection
   * @return customFieldSelectOptions
   */
  @javax.annotation.Nullable
  public List<String> getCustomFieldSelectOptions() {
    return customFieldSelectOptions;
  }

  public void setCustomFieldSelectOptions(List<String> customFieldSelectOptions) {
    this.customFieldSelectOptions = customFieldSelectOptions;
  }


  public CheckoutCustomFieldEditFields deletable(Boolean deletable) {
    this.deletable = deletable;
    return this;
  }

  /**
   * True if the CheckoutCustomField can be removed from the store
   * @return deletable
   */
  @javax.annotation.Nullable
  public Boolean getDeletable() {
    return deletable;
  }

  public void setDeletable(Boolean deletable) {
    this.deletable = deletable;
  }


  public CheckoutCustomFieldEditFields label(String label) {
    this.label = label;
    return this;
  }

  /**
   * Label given to the CheckoutCustomField
   * @return label
   */
  @javax.annotation.Nullable
  public String getLabel() {
    return label;
  }

  public void setLabel(String label) {
    this.label = label;
  }


  public CheckoutCustomFieldEditFields position(Integer position) {
    this.position = position;
    return this;
  }

  /**
   * Position of the CheckoutCustomField
   * @return position
   */
  @javax.annotation.Nullable
  public Integer getPosition() {
    return position;
  }

  public void setPosition(Integer position) {
    this.position = position;
  }


  public CheckoutCustomFieldEditFields required(Boolean required) {
    this.required = required;
    return this;
  }

  /**
   * True if the CheckoutCustomField is mandatory
   * @return required
   */
  @javax.annotation.Nullable
  public Boolean getRequired() {
    return required;
  }

  public void setRequired(Boolean required) {
    this.required = required;
  }


  public CheckoutCustomFieldEditFields type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Type of the CheckoutCustomField
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
    this.type = type;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CheckoutCustomFieldEditFields checkoutCustomFieldEditFields = (CheckoutCustomFieldEditFields) o;
    return Objects.equals(this.area, checkoutCustomFieldEditFields.area) &&
        Objects.equals(this.customFieldSelectOptions, checkoutCustomFieldEditFields.customFieldSelectOptions) &&
        Objects.equals(this.deletable, checkoutCustomFieldEditFields.deletable) &&
        Objects.equals(this.label, checkoutCustomFieldEditFields.label) &&
        Objects.equals(this.position, checkoutCustomFieldEditFields.position) &&
        Objects.equals(this.required, checkoutCustomFieldEditFields.required) &&
        Objects.equals(this.type, checkoutCustomFieldEditFields.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(area, customFieldSelectOptions, deletable, label, position, required, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CheckoutCustomFieldEditFields {\n");
    sb.append("    area: ").append(toIndentedString(area)).append("\n");
    sb.append("    customFieldSelectOptions: ").append(toIndentedString(customFieldSelectOptions)).append("\n");
    sb.append("    deletable: ").append(toIndentedString(deletable)).append("\n");
    sb.append("    label: ").append(toIndentedString(label)).append("\n");
    sb.append("    position: ").append(toIndentedString(position)).append("\n");
    sb.append("    required: ").append(toIndentedString(required)).append("\n");
    sb.append("    type: ").append(toIndentedString(type)).append("\n");
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
    openapiFields.add("area");
    openapiFields.add("custom_field_select_options");
    openapiFields.add("deletable");
    openapiFields.add("label");
    openapiFields.add("position");
    openapiFields.add("required");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CheckoutCustomFieldEditFields
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CheckoutCustomFieldEditFields.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CheckoutCustomFieldEditFields is not found in the empty JSON string", CheckoutCustomFieldEditFields.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CheckoutCustomFieldEditFields.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CheckoutCustomFieldEditFields` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("area") != null && !jsonObj.get("area").isJsonNull()) && !jsonObj.get("area").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `area` to be a primitive type in the JSON string but got `%s`", jsonObj.get("area").toString()));
      }
      // validate the optional field `area`
      if (jsonObj.get("area") != null && !jsonObj.get("area").isJsonNull()) {
        AreaEnum.validateJsonElement(jsonObj.get("area"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("custom_field_select_options") != null && !jsonObj.get("custom_field_select_options").isJsonNull() && !jsonObj.get("custom_field_select_options").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `custom_field_select_options` to be an array in the JSON string but got `%s`", jsonObj.get("custom_field_select_options").toString()));
      }
      if ((jsonObj.get("label") != null && !jsonObj.get("label").isJsonNull()) && !jsonObj.get("label").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `label` to be a primitive type in the JSON string but got `%s`", jsonObj.get("label").toString()));
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CheckoutCustomFieldEditFields.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CheckoutCustomFieldEditFields' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CheckoutCustomFieldEditFields> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CheckoutCustomFieldEditFields.class));

       return (TypeAdapter<T>) new TypeAdapter<CheckoutCustomFieldEditFields>() {
           @Override
           public void write(JsonWriter out, CheckoutCustomFieldEditFields value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CheckoutCustomFieldEditFields read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CheckoutCustomFieldEditFields given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CheckoutCustomFieldEditFields
   * @throws IOException if the JSON string is invalid with respect to CheckoutCustomFieldEditFields
   */
  public static CheckoutCustomFieldEditFields fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CheckoutCustomFieldEditFields.class);
  }

  /**
   * Convert an instance of CheckoutCustomFieldEditFields to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

