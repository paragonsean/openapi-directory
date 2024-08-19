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
import org.openapitools.client.model.OrderAdditionalFields;

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
 * OrderEditFields
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:37.537066-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OrderEditFields {
  public static final String SERIALIZED_NAME_ADDITIONAL_FIELDS = "additional_fields";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_FIELDS)
  private List<OrderAdditionalFields> additionalFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_ADDITIONAL_INFORMATION = "additional_information";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_INFORMATION)
  private String additionalInformation;

  /**
   * Status of the Order Shipping
   */
  @JsonAdapter(ShipmentStatusEnum.Adapter.class)
  public enum ShipmentStatusEnum {
    REQUESTED("requested"),
    
    IN_TRANSIT("in_transit"),
    
    DELIVERED("delivered"),
    
    FAILED("failed"),
    
    PICKUP_AVAILABLE("pickup_available");

    private String value;

    ShipmentStatusEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ShipmentStatusEnum fromValue(String value) {
      for (ShipmentStatusEnum b : ShipmentStatusEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ShipmentStatusEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ShipmentStatusEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ShipmentStatusEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ShipmentStatusEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ShipmentStatusEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SHIPMENT_STATUS = "shipment_status";
  @SerializedName(SERIALIZED_NAME_SHIPMENT_STATUS)
  private ShipmentStatusEnum shipmentStatus;

  /**
   * Status of the Order
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    ABANDONED("Abandoned"),
    
    CANCELED("Canceled"),
    
    PENDING_PAYMENT("Pending Payment"),
    
    PAID("Paid");

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

  public static final String SERIALIZED_NAME_TRACKING_COMPANY = "tracking_company";
  @SerializedName(SERIALIZED_NAME_TRACKING_COMPANY)
  private String trackingCompany;

  public static final String SERIALIZED_NAME_TRACKING_NUMBER = "tracking_number";
  @SerializedName(SERIALIZED_NAME_TRACKING_NUMBER)
  private String trackingNumber;

  public static final String SERIALIZED_NAME_TRACKING_URL = "tracking_url";
  @SerializedName(SERIALIZED_NAME_TRACKING_URL)
  private String trackingUrl;

  public OrderEditFields() {
  }

  public OrderEditFields additionalFields(List<OrderAdditionalFields> additionalFields) {
    this.additionalFields = additionalFields;
    return this;
  }

  public OrderEditFields addAdditionalFieldsItem(OrderAdditionalFields additionalFieldsItem) {
    if (this.additionalFields == null) {
      this.additionalFields = new ArrayList<>();
    }
    this.additionalFields.add(additionalFieldsItem);
    return this;
  }

  /**
   * Array of additional fields for the given Order
   * @return additionalFields
   */
  @javax.annotation.Nullable
  public List<OrderAdditionalFields> getAdditionalFields() {
    return additionalFields;
  }

  public void setAdditionalFields(List<OrderAdditionalFields> additionalFields) {
    this.additionalFields = additionalFields;
  }


  public OrderEditFields additionalInformation(String additionalInformation) {
    this.additionalInformation = additionalInformation;
    return this;
  }

  /**
   * Additional information for the given Order
   * @return additionalInformation
   */
  @javax.annotation.Nullable
  public String getAdditionalInformation() {
    return additionalInformation;
  }

  public void setAdditionalInformation(String additionalInformation) {
    this.additionalInformation = additionalInformation;
  }


  public OrderEditFields shipmentStatus(ShipmentStatusEnum shipmentStatus) {
    this.shipmentStatus = shipmentStatus;
    return this;
  }

  /**
   * Status of the Order Shipping
   * @return shipmentStatus
   */
  @javax.annotation.Nullable
  public ShipmentStatusEnum getShipmentStatus() {
    return shipmentStatus;
  }

  public void setShipmentStatus(ShipmentStatusEnum shipmentStatus) {
    this.shipmentStatus = shipmentStatus;
  }


  public OrderEditFields status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Status of the Order
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public OrderEditFields trackingCompany(String trackingCompany) {
    this.trackingCompany = trackingCompany;
    return this;
  }

  /**
   * Shipping Company used for the given Order
   * @return trackingCompany
   */
  @javax.annotation.Nullable
  public String getTrackingCompany() {
    return trackingCompany;
  }

  public void setTrackingCompany(String trackingCompany) {
    this.trackingCompany = trackingCompany;
  }


  public OrderEditFields trackingNumber(String trackingNumber) {
    this.trackingNumber = trackingNumber;
    return this;
  }

  /**
   * Shipping Tracking Number used for the given Order
   * @return trackingNumber
   */
  @javax.annotation.Nullable
  public String getTrackingNumber() {
    return trackingNumber;
  }

  public void setTrackingNumber(String trackingNumber) {
    this.trackingNumber = trackingNumber;
  }


  public OrderEditFields trackingUrl(String trackingUrl) {
    this.trackingUrl = trackingUrl;
    return this;
  }

  /**
   * URL to check delivery information for the given Order
   * @return trackingUrl
   */
  @javax.annotation.Nullable
  public String getTrackingUrl() {
    return trackingUrl;
  }

  public void setTrackingUrl(String trackingUrl) {
    this.trackingUrl = trackingUrl;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    OrderEditFields orderEditFields = (OrderEditFields) o;
    return Objects.equals(this.additionalFields, orderEditFields.additionalFields) &&
        Objects.equals(this.additionalInformation, orderEditFields.additionalInformation) &&
        Objects.equals(this.shipmentStatus, orderEditFields.shipmentStatus) &&
        Objects.equals(this.status, orderEditFields.status) &&
        Objects.equals(this.trackingCompany, orderEditFields.trackingCompany) &&
        Objects.equals(this.trackingNumber, orderEditFields.trackingNumber) &&
        Objects.equals(this.trackingUrl, orderEditFields.trackingUrl);
  }

  @Override
  public int hashCode() {
    return Objects.hash(additionalFields, additionalInformation, shipmentStatus, status, trackingCompany, trackingNumber, trackingUrl);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OrderEditFields {\n");
    sb.append("    additionalFields: ").append(toIndentedString(additionalFields)).append("\n");
    sb.append("    additionalInformation: ").append(toIndentedString(additionalInformation)).append("\n");
    sb.append("    shipmentStatus: ").append(toIndentedString(shipmentStatus)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    trackingCompany: ").append(toIndentedString(trackingCompany)).append("\n");
    sb.append("    trackingNumber: ").append(toIndentedString(trackingNumber)).append("\n");
    sb.append("    trackingUrl: ").append(toIndentedString(trackingUrl)).append("\n");
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
    openapiFields.add("additional_fields");
    openapiFields.add("additional_information");
    openapiFields.add("shipment_status");
    openapiFields.add("status");
    openapiFields.add("tracking_company");
    openapiFields.add("tracking_number");
    openapiFields.add("tracking_url");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to OrderEditFields
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrderEditFields.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrderEditFields is not found in the empty JSON string", OrderEditFields.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrderEditFields.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrderEditFields` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("additional_fields") != null && !jsonObj.get("additional_fields").isJsonNull()) {
        JsonArray jsonArrayadditionalFields = jsonObj.getAsJsonArray("additional_fields");
        if (jsonArrayadditionalFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("additional_fields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `additional_fields` to be an array in the JSON string but got `%s`", jsonObj.get("additional_fields").toString()));
          }

          // validate the optional field `additional_fields` (array)
          for (int i = 0; i < jsonArrayadditionalFields.size(); i++) {
            OrderAdditionalFields.validateJsonElement(jsonArrayadditionalFields.get(i));
          };
        }
      }
      if ((jsonObj.get("additional_information") != null && !jsonObj.get("additional_information").isJsonNull()) && !jsonObj.get("additional_information").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `additional_information` to be a primitive type in the JSON string but got `%s`", jsonObj.get("additional_information").toString()));
      }
      if ((jsonObj.get("shipment_status") != null && !jsonObj.get("shipment_status").isJsonNull()) && !jsonObj.get("shipment_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shipment_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shipment_status").toString()));
      }
      // validate the optional field `shipment_status`
      if (jsonObj.get("shipment_status") != null && !jsonObj.get("shipment_status").isJsonNull()) {
        ShipmentStatusEnum.validateJsonElement(jsonObj.get("shipment_status"));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if ((jsonObj.get("tracking_company") != null && !jsonObj.get("tracking_company").isJsonNull()) && !jsonObj.get("tracking_company").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tracking_company` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tracking_company").toString()));
      }
      if ((jsonObj.get("tracking_number") != null && !jsonObj.get("tracking_number").isJsonNull()) && !jsonObj.get("tracking_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tracking_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tracking_number").toString()));
      }
      if ((jsonObj.get("tracking_url") != null && !jsonObj.get("tracking_url").isJsonNull()) && !jsonObj.get("tracking_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tracking_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tracking_url").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!OrderEditFields.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrderEditFields' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrderEditFields> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrderEditFields.class));

       return (TypeAdapter<T>) new TypeAdapter<OrderEditFields>() {
           @Override
           public void write(JsonWriter out, OrderEditFields value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrderEditFields read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OrderEditFields given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OrderEditFields
   * @throws IOException if the JSON string is invalid with respect to OrderEditFields
   */
  public static OrderEditFields fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrderEditFields.class);
  }

  /**
   * Convert an instance of OrderEditFields to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

