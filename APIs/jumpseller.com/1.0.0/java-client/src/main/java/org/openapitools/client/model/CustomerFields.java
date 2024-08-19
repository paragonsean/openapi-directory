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
import org.openapitools.client.model.BillingAddress;
import org.openapitools.client.model.CustomerAdditionalField;
import org.openapitools.client.model.CustomerCategory;
import org.openapitools.client.model.ShippingAddress;

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
 * CustomerFields
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:37.537066-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CustomerFields {
  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billing_address";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private BillingAddress billingAddress;

  public static final String SERIALIZED_NAME_CUSTOMER_ADDITIONAL_FIELDS = "customer_additional_fields";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_ADDITIONAL_FIELDS)
  private List<CustomerAdditionalField> customerAdditionalFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUSTOMER_CATEGORIES = "customer_categories";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_CATEGORIES)
  private List<CustomerCategory> customerCategories = new ArrayList<>();

  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PHONE = "phone";
  @SerializedName(SERIALIZED_NAME_PHONE)
  private String phone;

  public static final String SERIALIZED_NAME_SHIPPING_ADDRESS = "shipping_address";
  @SerializedName(SERIALIZED_NAME_SHIPPING_ADDRESS)
  private ShippingAddress shippingAddress;

  /**
   * Status of the Customer
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    APPROVED("approved"),
    
    PENDING("pending"),
    
    DISABLED("disabled");

    private String value;

    StatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static StatusEnum fromValue(String value) {
      for (StatusEnum b : StatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<StatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final StatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public StatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return StatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      StatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private StatusEnum status;

  public static final String SERIALIZED_NAME_SURNAME = "surname";
  @SerializedName(SERIALIZED_NAME_SURNAME)
  private String surname;

  public CustomerFields() {
  }

  public CustomerFields billingAddress(BillingAddress billingAddress) {
    this.billingAddress = billingAddress;
    return this;
  }

  /**
   * Get billingAddress
   * @return billingAddress
   */
  @javax.annotation.Nullable
  public BillingAddress getBillingAddress() {
    return billingAddress;
  }

  public void setBillingAddress(BillingAddress billingAddress) {
    this.billingAddress = billingAddress;
  }


  public CustomerFields customerAdditionalFields(List<CustomerAdditionalField> customerAdditionalFields) {
    this.customerAdditionalFields = customerAdditionalFields;
    return this;
  }

  public CustomerFields addCustomerAdditionalFieldsItem(CustomerAdditionalField customerAdditionalFieldsItem) {
    if (this.customerAdditionalFields == null) {
      this.customerAdditionalFields = new ArrayList<>();
    }
    this.customerAdditionalFields.add(customerAdditionalFieldsItem);
    return this;
  }

  /**
   * Get customerAdditionalFields
   * @return customerAdditionalFields
   */
  @javax.annotation.Nullable
  public List<CustomerAdditionalField> getCustomerAdditionalFields() {
    return customerAdditionalFields;
  }

  public void setCustomerAdditionalFields(List<CustomerAdditionalField> customerAdditionalFields) {
    this.customerAdditionalFields = customerAdditionalFields;
  }


  public CustomerFields customerCategories(List<CustomerCategory> customerCategories) {
    this.customerCategories = customerCategories;
    return this;
  }

  public CustomerFields addCustomerCategoriesItem(CustomerCategory customerCategoriesItem) {
    if (this.customerCategories == null) {
      this.customerCategories = new ArrayList<>();
    }
    this.customerCategories.add(customerCategoriesItem);
    return this;
  }

  /**
   * Get customerCategories
   * @return customerCategories
   */
  @javax.annotation.Nullable
  public List<CustomerCategory> getCustomerCategories() {
    return customerCategories;
  }

  public void setCustomerCategories(List<CustomerCategory> customerCategories) {
    this.customerCategories = customerCategories;
  }


  public CustomerFields email(String email) {
    this.email = email;
    return this;
  }

  /**
   * Email of the Customer
   * @return email
   */
  @javax.annotation.Nullable
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  public CustomerFields id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Unique identifier of the Customer
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public CustomerFields name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of the Customer
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public CustomerFields phone(String phone) {
    this.phone = phone;
    return this;
  }

  /**
   * Phone of the Customer
   * @return phone
   */
  @javax.annotation.Nullable
  public String getPhone() {
    return phone;
  }

  public void setPhone(String phone) {
    this.phone = phone;
  }


  public CustomerFields shippingAddress(ShippingAddress shippingAddress) {
    this.shippingAddress = shippingAddress;
    return this;
  }

  /**
   * Get shippingAddress
   * @return shippingAddress
   */
  @javax.annotation.Nullable
  public ShippingAddress getShippingAddress() {
    return shippingAddress;
  }

  public void setShippingAddress(ShippingAddress shippingAddress) {
    this.shippingAddress = shippingAddress;
  }


  public CustomerFields status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Status of the Customer
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public CustomerFields surname(String surname) {
    this.surname = surname;
    return this;
  }

  /**
   * Surname of the Customer
   * @return surname
   */
  @javax.annotation.Nullable
  public String getSurname() {
    return surname;
  }

  public void setSurname(String surname) {
    this.surname = surname;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CustomerFields customerFields = (CustomerFields) o;
    return Objects.equals(this.billingAddress, customerFields.billingAddress) &&
        Objects.equals(this.customerAdditionalFields, customerFields.customerAdditionalFields) &&
        Objects.equals(this.customerCategories, customerFields.customerCategories) &&
        Objects.equals(this.email, customerFields.email) &&
        Objects.equals(this.id, customerFields.id) &&
        Objects.equals(this.name, customerFields.name) &&
        Objects.equals(this.phone, customerFields.phone) &&
        Objects.equals(this.shippingAddress, customerFields.shippingAddress) &&
        Objects.equals(this.status, customerFields.status) &&
        Objects.equals(this.surname, customerFields.surname);
  }

  @Override
  public int hashCode() {
    return Objects.hash(billingAddress, customerAdditionalFields, customerCategories, email, id, name, phone, shippingAddress, status, surname);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CustomerFields {\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    customerAdditionalFields: ").append(toIndentedString(customerAdditionalFields)).append("\n");
    sb.append("    customerCategories: ").append(toIndentedString(customerCategories)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    phone: ").append(toIndentedString(phone)).append("\n");
    sb.append("    shippingAddress: ").append(toIndentedString(shippingAddress)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    surname: ").append(toIndentedString(surname)).append("\n");
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
    openapiFields.add("billing_address");
    openapiFields.add("customer_additional_fields");
    openapiFields.add("customer_categories");
    openapiFields.add("email");
    openapiFields.add("id");
    openapiFields.add("name");
    openapiFields.add("phone");
    openapiFields.add("shipping_address");
    openapiFields.add("status");
    openapiFields.add("surname");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CustomerFields
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CustomerFields.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CustomerFields is not found in the empty JSON string", CustomerFields.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CustomerFields.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CustomerFields` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `billing_address`
      if (jsonObj.get("billing_address") != null && !jsonObj.get("billing_address").isJsonNull()) {
        BillingAddress.validateJsonElement(jsonObj.get("billing_address"));
      }
      if (jsonObj.get("customer_additional_fields") != null && !jsonObj.get("customer_additional_fields").isJsonNull()) {
        JsonArray jsonArraycustomerAdditionalFields = jsonObj.getAsJsonArray("customer_additional_fields");
        if (jsonArraycustomerAdditionalFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("customer_additional_fields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `customer_additional_fields` to be an array in the JSON string but got `%s`", jsonObj.get("customer_additional_fields").toString()));
          }

          // validate the optional field `customer_additional_fields` (array)
          for (int i = 0; i < jsonArraycustomerAdditionalFields.size(); i++) {
            CustomerAdditionalField.validateJsonElement(jsonArraycustomerAdditionalFields.get(i));
          };
        }
      }
      if (jsonObj.get("customer_categories") != null && !jsonObj.get("customer_categories").isJsonNull()) {
        JsonArray jsonArraycustomerCategories = jsonObj.getAsJsonArray("customer_categories");
        if (jsonArraycustomerCategories != null) {
          // ensure the json data is an array
          if (!jsonObj.get("customer_categories").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `customer_categories` to be an array in the JSON string but got `%s`", jsonObj.get("customer_categories").toString()));
          }

          // validate the optional field `customer_categories` (array)
          for (int i = 0; i < jsonArraycustomerCategories.size(); i++) {
            CustomerCategory.validateJsonElement(jsonArraycustomerCategories.get(i));
          };
        }
      }
      if ((jsonObj.get("email") != null && !jsonObj.get("email").isJsonNull()) && !jsonObj.get("email").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `email` to be a primitive type in the JSON string but got `%s`", jsonObj.get("email").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("phone") != null && !jsonObj.get("phone").isJsonNull()) && !jsonObj.get("phone").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `phone` to be a primitive type in the JSON string but got `%s`", jsonObj.get("phone").toString()));
      }
      // validate the optional field `shipping_address`
      if (jsonObj.get("shipping_address") != null && !jsonObj.get("shipping_address").isJsonNull()) {
        ShippingAddress.validateJsonElement(jsonObj.get("shipping_address"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if ((jsonObj.get("surname") != null && !jsonObj.get("surname").isJsonNull()) && !jsonObj.get("surname").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `surname` to be a primitive type in the JSON string but got `%s`", jsonObj.get("surname").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CustomerFields.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CustomerFields' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CustomerFields> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CustomerFields.class));

       return (TypeAdapter<T>) new TypeAdapter<CustomerFields>() {
           @Override
           public void write(JsonWriter out, CustomerFields value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CustomerFields read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CustomerFields given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CustomerFields
   * @throws IOException if the JSON string is invalid with respect to CustomerFields
   */
  public static CustomerFields fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CustomerFields.class);
  }

  /**
   * Convert an instance of CustomerFields to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

