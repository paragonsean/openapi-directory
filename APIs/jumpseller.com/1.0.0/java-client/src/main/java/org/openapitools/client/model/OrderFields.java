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
import org.openapitools.client.model.Customer;
import org.openapitools.client.model.OrderAdditionalFields;
import org.openapitools.client.model.OrderBillingAddress;
import org.openapitools.client.model.OrderProduct;
import org.openapitools.client.model.OrderShippingAddress;
import org.openapitools.client.model.OrderShippingTax;
import org.openapitools.client.model.TrafficSource;

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
 * OrderFields
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:37.537066-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class OrderFields {
  public static final String SERIALIZED_NAME_ADDITIONAL_FIELDS = "additional_fields";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_FIELDS)
  private List<OrderAdditionalFields> additionalFields = new ArrayList<>();

  public static final String SERIALIZED_NAME_ADDITIONAL_INFORMATION = "additional_information";
  @SerializedName(SERIALIZED_NAME_ADDITIONAL_INFORMATION)
  private String additionalInformation;

  public static final String SERIALIZED_NAME_BILLING_ADDRESS = "billing_address";
  @SerializedName(SERIALIZED_NAME_BILLING_ADDRESS)
  private OrderBillingAddress billingAddress;

  public static final String SERIALIZED_NAME_CHECKOUT_URL = "checkout_url";
  @SerializedName(SERIALIZED_NAME_CHECKOUT_URL)
  private String checkoutUrl;

  public static final String SERIALIZED_NAME_COUPONS = "coupons";
  @SerializedName(SERIALIZED_NAME_COUPONS)
  private String coupons;

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_CUSTOMER = "customer";
  @SerializedName(SERIALIZED_NAME_CUSTOMER)
  private Customer customer;

  public static final String SERIALIZED_NAME_DISCOUNT = "discount";
  @SerializedName(SERIALIZED_NAME_DISCOUNT)
  private Float discount;

  public static final String SERIALIZED_NAME_DUPLICATE_URL = "duplicate_url";
  @SerializedName(SERIALIZED_NAME_DUPLICATE_URL)
  private String duplicateUrl;

  public static final String SERIALIZED_NAME_EXTERNAL_SHIPPING_RATE_ID = "external_shipping_rate_id";
  @SerializedName(SERIALIZED_NAME_EXTERNAL_SHIPPING_RATE_ID)
  private String externalShippingRateId;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_PAYMENT_INFORMATION = "payment_information";
  @SerializedName(SERIALIZED_NAME_PAYMENT_INFORMATION)
  private String paymentInformation;

  public static final String SERIALIZED_NAME_PAYMENT_METHOD_NAME = "payment_method_name";
  @SerializedName(SERIALIZED_NAME_PAYMENT_METHOD_NAME)
  private String paymentMethodName;

  public static final String SERIALIZED_NAME_PAYMENT_METHOD_TYPE = "payment_method_type";
  @SerializedName(SERIALIZED_NAME_PAYMENT_METHOD_TYPE)
  private String paymentMethodType;

  public static final String SERIALIZED_NAME_PRODUCTS = "products";
  @SerializedName(SERIALIZED_NAME_PRODUCTS)
  private List<OrderProduct> products = new ArrayList<>();

  public static final String SERIALIZED_NAME_RECOVERY_URL = "recovery_url";
  @SerializedName(SERIALIZED_NAME_RECOVERY_URL)
  private String recoveryUrl;

  /**
   * Shipment Status for Order Fulfillment.
   */
  @JsonAdapter(ShipmentStatusEnum.Adapter.class)
  public enum ShipmentStatusEnum {
    DELIVERED("delivered"),
    
    REQUESTED("requested"),
    
    IN_TRANSIT("in_transit"),
    
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

  public static final String SERIALIZED_NAME_SHIPPING = "shipping";
  @SerializedName(SERIALIZED_NAME_SHIPPING)
  private Float shipping;

  public static final String SERIALIZED_NAME_SHIPPING_ADDRESS = "shipping_address";
  @SerializedName(SERIALIZED_NAME_SHIPPING_ADDRESS)
  private OrderShippingAddress shippingAddress;

  public static final String SERIALIZED_NAME_SHIPPING_DISCOUNT = "shipping_discount";
  @SerializedName(SERIALIZED_NAME_SHIPPING_DISCOUNT)
  private Float shippingDiscount;

  public static final String SERIALIZED_NAME_SHIPPING_METHOD_ID = "shipping_method_id";
  @SerializedName(SERIALIZED_NAME_SHIPPING_METHOD_ID)
  private Integer shippingMethodId;

  public static final String SERIALIZED_NAME_SHIPPING_METHOD_NAME = "shipping_method_name";
  @SerializedName(SERIALIZED_NAME_SHIPPING_METHOD_NAME)
  private String shippingMethodName;

  /**
   * Shipping option for this order.
   */
  @JsonAdapter(ShippingOptionEnum.Adapter.class)
  public enum ShippingOptionEnum {
    DELIVERY("delivery"),
    
    STORE_PICKUP("store_pickup"),
    
    NO_SHIPPING("no_shipping");

    private String value;

    ShippingOptionEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static ShippingOptionEnum fromValue(String value) {
      for (ShippingOptionEnum b : ShippingOptionEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<ShippingOptionEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final ShippingOptionEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public ShippingOptionEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return ShippingOptionEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      ShippingOptionEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_SHIPPING_OPTION = "shipping_option";
  @SerializedName(SERIALIZED_NAME_SHIPPING_OPTION)
  private ShippingOptionEnum shippingOption;

  public static final String SERIALIZED_NAME_SHIPPING_REQUIRED = "shipping_required";
  @SerializedName(SERIALIZED_NAME_SHIPPING_REQUIRED)
  private Boolean shippingRequired = true;

  public static final String SERIALIZED_NAME_SHIPPING_TAX = "shipping_tax";
  @SerializedName(SERIALIZED_NAME_SHIPPING_TAX)
  private Float shippingTax;

  public static final String SERIALIZED_NAME_SHIPPING_TAXES = "shipping_taxes";
  @SerializedName(SERIALIZED_NAME_SHIPPING_TAXES)
  private List<OrderShippingTax> shippingTaxes = new ArrayList<>();

  public static final String SERIALIZED_NAME_SOURCE = "source";
  @SerializedName(SERIALIZED_NAME_SOURCE)
  private TrafficSource source;

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

  public static final String SERIALIZED_NAME_SUBTOTAL = "subtotal";
  @SerializedName(SERIALIZED_NAME_SUBTOTAL)
  private Float subtotal;

  public static final String SERIALIZED_NAME_TAX = "tax";
  @SerializedName(SERIALIZED_NAME_TAX)
  private Float tax;

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private Float total;

  public static final String SERIALIZED_NAME_TRACKING_COMPANY = "tracking_company";
  @SerializedName(SERIALIZED_NAME_TRACKING_COMPANY)
  private String trackingCompany;

  public static final String SERIALIZED_NAME_TRACKING_NUMBER = "tracking_number";
  @SerializedName(SERIALIZED_NAME_TRACKING_NUMBER)
  private String trackingNumber;

  public static final String SERIALIZED_NAME_TRACKING_URL = "tracking_url";
  @SerializedName(SERIALIZED_NAME_TRACKING_URL)
  private String trackingUrl;

  public OrderFields() {
  }

  public OrderFields additionalFields(List<OrderAdditionalFields> additionalFields) {
    this.additionalFields = additionalFields;
    return this;
  }

  public OrderFields addAdditionalFieldsItem(OrderAdditionalFields additionalFieldsItem) {
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


  public OrderFields additionalInformation(String additionalInformation) {
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


  public OrderFields billingAddress(OrderBillingAddress billingAddress) {
    this.billingAddress = billingAddress;
    return this;
  }

  /**
   * Get billingAddress
   * @return billingAddress
   */
  @javax.annotation.Nullable
  public OrderBillingAddress getBillingAddress() {
    return billingAddress;
  }

  public void setBillingAddress(OrderBillingAddress billingAddress) {
    this.billingAddress = billingAddress;
  }


  public OrderFields checkoutUrl(String checkoutUrl) {
    this.checkoutUrl = checkoutUrl;
    return this;
  }

  /**
   * Store Checkout Order URL for the given Order
   * @return checkoutUrl
   */
  @javax.annotation.Nullable
  public String getCheckoutUrl() {
    return checkoutUrl;
  }

  public void setCheckoutUrl(String checkoutUrl) {
    this.checkoutUrl = checkoutUrl;
  }


  public OrderFields coupons(String coupons) {
    this.coupons = coupons;
    return this;
  }

  /**
   * Promotion Coupons used on the given Order
   * @return coupons
   */
  @javax.annotation.Nullable
  public String getCoupons() {
    return coupons;
  }

  public void setCoupons(String coupons) {
    this.coupons = coupons;
  }


  public OrderFields createdAt(String createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Order date
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(String createdAt) {
    this.createdAt = createdAt;
  }


  public OrderFields currency(String currency) {
    this.currency = currency;
    return this;
  }

  /**
   * Currency of the Order
   * @return currency
   */
  @javax.annotation.Nullable
  public String getCurrency() {
    return currency;
  }

  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public OrderFields customer(Customer customer) {
    this.customer = customer;
    return this;
  }

  /**
   * Get customer
   * @return customer
   */
  @javax.annotation.Nullable
  public Customer getCustomer() {
    return customer;
  }

  public void setCustomer(Customer customer) {
    this.customer = customer;
  }


  public OrderFields discount(Float discount) {
    this.discount = discount;
    return this;
  }

  /**
   * Discount value for the given Order
   * @return discount
   */
  @javax.annotation.Nullable
  public Float getDiscount() {
    return discount;
  }

  public void setDiscount(Float discount) {
    this.discount = discount;
  }


  public OrderFields duplicateUrl(String duplicateUrl) {
    this.duplicateUrl = duplicateUrl;
    return this;
  }

  /**
   * Duplicate Order URL for the given Order
   * @return duplicateUrl
   */
  @javax.annotation.Nullable
  public String getDuplicateUrl() {
    return duplicateUrl;
  }

  public void setDuplicateUrl(String duplicateUrl) {
    this.duplicateUrl = duplicateUrl;
  }


  public OrderFields externalShippingRateId(String externalShippingRateId) {
    this.externalShippingRateId = externalShippingRateId;
    return this;
  }

  /**
   * Rate id for selected External Shipping Method rate
   * @return externalShippingRateId
   */
  @javax.annotation.Nullable
  public String getExternalShippingRateId() {
    return externalShippingRateId;
  }

  public void setExternalShippingRateId(String externalShippingRateId) {
    this.externalShippingRateId = externalShippingRateId;
  }


  public OrderFields id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Unique identifier of the Order
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public OrderFields paymentInformation(String paymentInformation) {
    this.paymentInformation = paymentInformation;
    return this;
  }

  /**
   * Payment information for the given Order
   * @return paymentInformation
   */
  @javax.annotation.Nullable
  public String getPaymentInformation() {
    return paymentInformation;
  }

  public void setPaymentInformation(String paymentInformation) {
    this.paymentInformation = paymentInformation;
  }


  public OrderFields paymentMethodName(String paymentMethodName) {
    this.paymentMethodName = paymentMethodName;
    return this;
  }

  /**
   * Payment Method name used e.g. PayPal
   * @return paymentMethodName
   */
  @javax.annotation.Nullable
  public String getPaymentMethodName() {
    return paymentMethodName;
  }

  public void setPaymentMethodName(String paymentMethodName) {
    this.paymentMethodName = paymentMethodName;
  }


  public OrderFields paymentMethodType(String paymentMethodType) {
    this.paymentMethodType = paymentMethodType;
    return this;
  }

  /**
   * Payment Method type used e.g. paypal
   * @return paymentMethodType
   */
  @javax.annotation.Nullable
  public String getPaymentMethodType() {
    return paymentMethodType;
  }

  public void setPaymentMethodType(String paymentMethodType) {
    this.paymentMethodType = paymentMethodType;
  }


  public OrderFields products(List<OrderProduct> products) {
    this.products = products;
    return this;
  }

  public OrderFields addProductsItem(OrderProduct productsItem) {
    if (this.products == null) {
      this.products = new ArrayList<>();
    }
    this.products.add(productsItem);
    return this;
  }

  /**
   * Get products
   * @return products
   */
  @javax.annotation.Nullable
  public List<OrderProduct> getProducts() {
    return products;
  }

  public void setProducts(List<OrderProduct> products) {
    this.products = products;
  }


  public OrderFields recoveryUrl(String recoveryUrl) {
    this.recoveryUrl = recoveryUrl;
    return this;
  }

  /**
   * Recovery Order URL for the given Order
   * @return recoveryUrl
   */
  @javax.annotation.Nullable
  public String getRecoveryUrl() {
    return recoveryUrl;
  }

  public void setRecoveryUrl(String recoveryUrl) {
    this.recoveryUrl = recoveryUrl;
  }


  public OrderFields shipmentStatus(ShipmentStatusEnum shipmentStatus) {
    this.shipmentStatus = shipmentStatus;
    return this;
  }

  /**
   * Shipment Status for Order Fulfillment.
   * @return shipmentStatus
   */
  @javax.annotation.Nullable
  public ShipmentStatusEnum getShipmentStatus() {
    return shipmentStatus;
  }

  public void setShipmentStatus(ShipmentStatusEnum shipmentStatus) {
    this.shipmentStatus = shipmentStatus;
  }


  public OrderFields shipping(Float shipping) {
    this.shipping = shipping;
    return this;
  }

  /**
   * Shipping value for the given Order
   * @return shipping
   */
  @javax.annotation.Nullable
  public Float getShipping() {
    return shipping;
  }

  public void setShipping(Float shipping) {
    this.shipping = shipping;
  }


  public OrderFields shippingAddress(OrderShippingAddress shippingAddress) {
    this.shippingAddress = shippingAddress;
    return this;
  }

  /**
   * Get shippingAddress
   * @return shippingAddress
   */
  @javax.annotation.Nullable
  public OrderShippingAddress getShippingAddress() {
    return shippingAddress;
  }

  public void setShippingAddress(OrderShippingAddress shippingAddress) {
    this.shippingAddress = shippingAddress;
  }


  public OrderFields shippingDiscount(Float shippingDiscount) {
    this.shippingDiscount = shippingDiscount;
    return this;
  }

  /**
   * Shipping Discount value for the given order
   * @return shippingDiscount
   */
  @javax.annotation.Nullable
  public Float getShippingDiscount() {
    return shippingDiscount;
  }

  public void setShippingDiscount(Float shippingDiscount) {
    this.shippingDiscount = shippingDiscount;
  }


  public OrderFields shippingMethodId(Integer shippingMethodId) {
    this.shippingMethodId = shippingMethodId;
    return this;
  }

  /**
   * Shipping method e.g. Royal Mail
   * @return shippingMethodId
   */
  @javax.annotation.Nullable
  public Integer getShippingMethodId() {
    return shippingMethodId;
  }

  public void setShippingMethodId(Integer shippingMethodId) {
    this.shippingMethodId = shippingMethodId;
  }


  public OrderFields shippingMethodName(String shippingMethodName) {
    this.shippingMethodName = shippingMethodName;
    return this;
  }

  /**
   * Shipping method e.g. Royal Mail
   * @return shippingMethodName
   */
  @javax.annotation.Nullable
  public String getShippingMethodName() {
    return shippingMethodName;
  }

  public void setShippingMethodName(String shippingMethodName) {
    this.shippingMethodName = shippingMethodName;
  }


  public OrderFields shippingOption(ShippingOptionEnum shippingOption) {
    this.shippingOption = shippingOption;
    return this;
  }

  /**
   * Shipping option for this order.
   * @return shippingOption
   */
  @javax.annotation.Nullable
  public ShippingOptionEnum getShippingOption() {
    return shippingOption;
  }

  public void setShippingOption(ShippingOptionEnum shippingOption) {
    this.shippingOption = shippingOption;
  }


  public OrderFields shippingRequired(Boolean shippingRequired) {
    this.shippingRequired = shippingRequired;
    return this;
  }

  /**
   * False if the order is digital.
   * @return shippingRequired
   */
  @javax.annotation.Nullable
  public Boolean getShippingRequired() {
    return shippingRequired;
  }

  public void setShippingRequired(Boolean shippingRequired) {
    this.shippingRequired = shippingRequired;
  }


  public OrderFields shippingTax(Float shippingTax) {
    this.shippingTax = shippingTax;
    return this;
  }

  /**
   * Shipping Tax value for the given order
   * @return shippingTax
   */
  @javax.annotation.Nullable
  public Float getShippingTax() {
    return shippingTax;
  }

  public void setShippingTax(Float shippingTax) {
    this.shippingTax = shippingTax;
  }


  public OrderFields shippingTaxes(List<OrderShippingTax> shippingTaxes) {
    this.shippingTaxes = shippingTaxes;
    return this;
  }

  public OrderFields addShippingTaxesItem(OrderShippingTax shippingTaxesItem) {
    if (this.shippingTaxes == null) {
      this.shippingTaxes = new ArrayList<>();
    }
    this.shippingTaxes.add(shippingTaxesItem);
    return this;
  }

  /**
   * Get shippingTaxes
   * @return shippingTaxes
   */
  @javax.annotation.Nullable
  public List<OrderShippingTax> getShippingTaxes() {
    return shippingTaxes;
  }

  public void setShippingTaxes(List<OrderShippingTax> shippingTaxes) {
    this.shippingTaxes = shippingTaxes;
  }


  public OrderFields source(TrafficSource source) {
    this.source = source;
    return this;
  }

  /**
   * Get source
   * @return source
   */
  @javax.annotation.Nullable
  public TrafficSource getSource() {
    return source;
  }

  public void setSource(TrafficSource source) {
    this.source = source;
  }


  public OrderFields status(StatusEnum status) {
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


  public OrderFields subtotal(Float subtotal) {
    this.subtotal = subtotal;
    return this;
  }

  /**
   * Subtotal value for the given Order. Excluding taxes, shipping and discounts
   * @return subtotal
   */
  @javax.annotation.Nullable
  public Float getSubtotal() {
    return subtotal;
  }

  public void setSubtotal(Float subtotal) {
    this.subtotal = subtotal;
  }


  public OrderFields tax(Float tax) {
    this.tax = tax;
    return this;
  }

  /**
   * Tax value for the given order
   * @return tax
   */
  @javax.annotation.Nullable
  public Float getTax() {
    return tax;
  }

  public void setTax(Float tax) {
    this.tax = tax;
  }


  public OrderFields total(Float total) {
    this.total = total;
    return this;
  }

  /**
   * Total value for the given Order. Including taxes, shipping and discounts
   * @return total
   */
  @javax.annotation.Nullable
  public Float getTotal() {
    return total;
  }

  public void setTotal(Float total) {
    this.total = total;
  }


  public OrderFields trackingCompany(String trackingCompany) {
    this.trackingCompany = trackingCompany;
    return this;
  }

  /**
   * Company Used for Order Fulfillment.
   * @return trackingCompany
   */
  @javax.annotation.Nullable
  public String getTrackingCompany() {
    return trackingCompany;
  }

  public void setTrackingCompany(String trackingCompany) {
    this.trackingCompany = trackingCompany;
  }


  public OrderFields trackingNumber(String trackingNumber) {
    this.trackingNumber = trackingNumber;
    return this;
  }

  /**
   * Tracking Number for Order Fulfillment.
   * @return trackingNumber
   */
  @javax.annotation.Nullable
  public String getTrackingNumber() {
    return trackingNumber;
  }

  public void setTrackingNumber(String trackingNumber) {
    this.trackingNumber = trackingNumber;
  }


  public OrderFields trackingUrl(String trackingUrl) {
    this.trackingUrl = trackingUrl;
    return this;
  }

  /**
   * Tracking URL for Order Fulfillment.
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
    OrderFields orderFields = (OrderFields) o;
    return Objects.equals(this.additionalFields, orderFields.additionalFields) &&
        Objects.equals(this.additionalInformation, orderFields.additionalInformation) &&
        Objects.equals(this.billingAddress, orderFields.billingAddress) &&
        Objects.equals(this.checkoutUrl, orderFields.checkoutUrl) &&
        Objects.equals(this.coupons, orderFields.coupons) &&
        Objects.equals(this.createdAt, orderFields.createdAt) &&
        Objects.equals(this.currency, orderFields.currency) &&
        Objects.equals(this.customer, orderFields.customer) &&
        Objects.equals(this.discount, orderFields.discount) &&
        Objects.equals(this.duplicateUrl, orderFields.duplicateUrl) &&
        Objects.equals(this.externalShippingRateId, orderFields.externalShippingRateId) &&
        Objects.equals(this.id, orderFields.id) &&
        Objects.equals(this.paymentInformation, orderFields.paymentInformation) &&
        Objects.equals(this.paymentMethodName, orderFields.paymentMethodName) &&
        Objects.equals(this.paymentMethodType, orderFields.paymentMethodType) &&
        Objects.equals(this.products, orderFields.products) &&
        Objects.equals(this.recoveryUrl, orderFields.recoveryUrl) &&
        Objects.equals(this.shipmentStatus, orderFields.shipmentStatus) &&
        Objects.equals(this.shipping, orderFields.shipping) &&
        Objects.equals(this.shippingAddress, orderFields.shippingAddress) &&
        Objects.equals(this.shippingDiscount, orderFields.shippingDiscount) &&
        Objects.equals(this.shippingMethodId, orderFields.shippingMethodId) &&
        Objects.equals(this.shippingMethodName, orderFields.shippingMethodName) &&
        Objects.equals(this.shippingOption, orderFields.shippingOption) &&
        Objects.equals(this.shippingRequired, orderFields.shippingRequired) &&
        Objects.equals(this.shippingTax, orderFields.shippingTax) &&
        Objects.equals(this.shippingTaxes, orderFields.shippingTaxes) &&
        Objects.equals(this.source, orderFields.source) &&
        Objects.equals(this.status, orderFields.status) &&
        Objects.equals(this.subtotal, orderFields.subtotal) &&
        Objects.equals(this.tax, orderFields.tax) &&
        Objects.equals(this.total, orderFields.total) &&
        Objects.equals(this.trackingCompany, orderFields.trackingCompany) &&
        Objects.equals(this.trackingNumber, orderFields.trackingNumber) &&
        Objects.equals(this.trackingUrl, orderFields.trackingUrl);
  }

  @Override
  public int hashCode() {
    return Objects.hash(additionalFields, additionalInformation, billingAddress, checkoutUrl, coupons, createdAt, currency, customer, discount, duplicateUrl, externalShippingRateId, id, paymentInformation, paymentMethodName, paymentMethodType, products, recoveryUrl, shipmentStatus, shipping, shippingAddress, shippingDiscount, shippingMethodId, shippingMethodName, shippingOption, shippingRequired, shippingTax, shippingTaxes, source, status, subtotal, tax, total, trackingCompany, trackingNumber, trackingUrl);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class OrderFields {\n");
    sb.append("    additionalFields: ").append(toIndentedString(additionalFields)).append("\n");
    sb.append("    additionalInformation: ").append(toIndentedString(additionalInformation)).append("\n");
    sb.append("    billingAddress: ").append(toIndentedString(billingAddress)).append("\n");
    sb.append("    checkoutUrl: ").append(toIndentedString(checkoutUrl)).append("\n");
    sb.append("    coupons: ").append(toIndentedString(coupons)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    customer: ").append(toIndentedString(customer)).append("\n");
    sb.append("    discount: ").append(toIndentedString(discount)).append("\n");
    sb.append("    duplicateUrl: ").append(toIndentedString(duplicateUrl)).append("\n");
    sb.append("    externalShippingRateId: ").append(toIndentedString(externalShippingRateId)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    paymentInformation: ").append(toIndentedString(paymentInformation)).append("\n");
    sb.append("    paymentMethodName: ").append(toIndentedString(paymentMethodName)).append("\n");
    sb.append("    paymentMethodType: ").append(toIndentedString(paymentMethodType)).append("\n");
    sb.append("    products: ").append(toIndentedString(products)).append("\n");
    sb.append("    recoveryUrl: ").append(toIndentedString(recoveryUrl)).append("\n");
    sb.append("    shipmentStatus: ").append(toIndentedString(shipmentStatus)).append("\n");
    sb.append("    shipping: ").append(toIndentedString(shipping)).append("\n");
    sb.append("    shippingAddress: ").append(toIndentedString(shippingAddress)).append("\n");
    sb.append("    shippingDiscount: ").append(toIndentedString(shippingDiscount)).append("\n");
    sb.append("    shippingMethodId: ").append(toIndentedString(shippingMethodId)).append("\n");
    sb.append("    shippingMethodName: ").append(toIndentedString(shippingMethodName)).append("\n");
    sb.append("    shippingOption: ").append(toIndentedString(shippingOption)).append("\n");
    sb.append("    shippingRequired: ").append(toIndentedString(shippingRequired)).append("\n");
    sb.append("    shippingTax: ").append(toIndentedString(shippingTax)).append("\n");
    sb.append("    shippingTaxes: ").append(toIndentedString(shippingTaxes)).append("\n");
    sb.append("    source: ").append(toIndentedString(source)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    subtotal: ").append(toIndentedString(subtotal)).append("\n");
    sb.append("    tax: ").append(toIndentedString(tax)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
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
    openapiFields.add("billing_address");
    openapiFields.add("checkout_url");
    openapiFields.add("coupons");
    openapiFields.add("created_at");
    openapiFields.add("currency");
    openapiFields.add("customer");
    openapiFields.add("discount");
    openapiFields.add("duplicate_url");
    openapiFields.add("external_shipping_rate_id");
    openapiFields.add("id");
    openapiFields.add("payment_information");
    openapiFields.add("payment_method_name");
    openapiFields.add("payment_method_type");
    openapiFields.add("products");
    openapiFields.add("recovery_url");
    openapiFields.add("shipment_status");
    openapiFields.add("shipping");
    openapiFields.add("shipping_address");
    openapiFields.add("shipping_discount");
    openapiFields.add("shipping_method_id");
    openapiFields.add("shipping_method_name");
    openapiFields.add("shipping_option");
    openapiFields.add("shipping_required");
    openapiFields.add("shipping_tax");
    openapiFields.add("shipping_taxes");
    openapiFields.add("source");
    openapiFields.add("status");
    openapiFields.add("subtotal");
    openapiFields.add("tax");
    openapiFields.add("total");
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
   * @throws IOException if the JSON Element is invalid with respect to OrderFields
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!OrderFields.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in OrderFields is not found in the empty JSON string", OrderFields.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!OrderFields.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `OrderFields` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
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
      // validate the optional field `billing_address`
      if (jsonObj.get("billing_address") != null && !jsonObj.get("billing_address").isJsonNull()) {
        OrderBillingAddress.validateJsonElement(jsonObj.get("billing_address"));
      }
      if ((jsonObj.get("checkout_url") != null && !jsonObj.get("checkout_url").isJsonNull()) && !jsonObj.get("checkout_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `checkout_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("checkout_url").toString()));
      }
      if ((jsonObj.get("coupons") != null && !jsonObj.get("coupons").isJsonNull()) && !jsonObj.get("coupons").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `coupons` to be a primitive type in the JSON string but got `%s`", jsonObj.get("coupons").toString()));
      }
      if ((jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) && !jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
      if ((jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonNull()) && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      // validate the optional field `customer`
      if (jsonObj.get("customer") != null && !jsonObj.get("customer").isJsonNull()) {
        Customer.validateJsonElement(jsonObj.get("customer"));
      }
      if ((jsonObj.get("duplicate_url") != null && !jsonObj.get("duplicate_url").isJsonNull()) && !jsonObj.get("duplicate_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `duplicate_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("duplicate_url").toString()));
      }
      if ((jsonObj.get("external_shipping_rate_id") != null && !jsonObj.get("external_shipping_rate_id").isJsonNull()) && !jsonObj.get("external_shipping_rate_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `external_shipping_rate_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("external_shipping_rate_id").toString()));
      }
      if ((jsonObj.get("payment_information") != null && !jsonObj.get("payment_information").isJsonNull()) && !jsonObj.get("payment_information").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_information` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_information").toString()));
      }
      if ((jsonObj.get("payment_method_name") != null && !jsonObj.get("payment_method_name").isJsonNull()) && !jsonObj.get("payment_method_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_method_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_method_name").toString()));
      }
      if ((jsonObj.get("payment_method_type") != null && !jsonObj.get("payment_method_type").isJsonNull()) && !jsonObj.get("payment_method_type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `payment_method_type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("payment_method_type").toString()));
      }
      if (jsonObj.get("products") != null && !jsonObj.get("products").isJsonNull()) {
        JsonArray jsonArrayproducts = jsonObj.getAsJsonArray("products");
        if (jsonArrayproducts != null) {
          // ensure the json data is an array
          if (!jsonObj.get("products").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `products` to be an array in the JSON string but got `%s`", jsonObj.get("products").toString()));
          }

          // validate the optional field `products` (array)
          for (int i = 0; i < jsonArrayproducts.size(); i++) {
            OrderProduct.validateJsonElement(jsonArrayproducts.get(i));
          };
        }
      }
      if ((jsonObj.get("recovery_url") != null && !jsonObj.get("recovery_url").isJsonNull()) && !jsonObj.get("recovery_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `recovery_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("recovery_url").toString()));
      }
      if ((jsonObj.get("shipment_status") != null && !jsonObj.get("shipment_status").isJsonNull()) && !jsonObj.get("shipment_status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shipment_status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shipment_status").toString()));
      }
      // validate the optional field `shipment_status`
      if (jsonObj.get("shipment_status") != null && !jsonObj.get("shipment_status").isJsonNull()) {
        ShipmentStatusEnum.validateJsonElement(jsonObj.get("shipment_status"));
      }
      // validate the optional field `shipping_address`
      if (jsonObj.get("shipping_address") != null && !jsonObj.get("shipping_address").isJsonNull()) {
        OrderShippingAddress.validateJsonElement(jsonObj.get("shipping_address"));
      }
      if ((jsonObj.get("shipping_method_name") != null && !jsonObj.get("shipping_method_name").isJsonNull()) && !jsonObj.get("shipping_method_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shipping_method_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shipping_method_name").toString()));
      }
      if ((jsonObj.get("shipping_option") != null && !jsonObj.get("shipping_option").isJsonNull()) && !jsonObj.get("shipping_option").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shipping_option` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shipping_option").toString()));
      }
      // validate the optional field `shipping_option`
      if (jsonObj.get("shipping_option") != null && !jsonObj.get("shipping_option").isJsonNull()) {
        ShippingOptionEnum.validateJsonElement(jsonObj.get("shipping_option"));
      }
      if (jsonObj.get("shipping_taxes") != null && !jsonObj.get("shipping_taxes").isJsonNull()) {
        JsonArray jsonArrayshippingTaxes = jsonObj.getAsJsonArray("shipping_taxes");
        if (jsonArrayshippingTaxes != null) {
          // ensure the json data is an array
          if (!jsonObj.get("shipping_taxes").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `shipping_taxes` to be an array in the JSON string but got `%s`", jsonObj.get("shipping_taxes").toString()));
          }

          // validate the optional field `shipping_taxes` (array)
          for (int i = 0; i < jsonArrayshippingTaxes.size(); i++) {
            OrderShippingTax.validateJsonElement(jsonArrayshippingTaxes.get(i));
          };
        }
      }
      // validate the optional field `source`
      if (jsonObj.get("source") != null && !jsonObj.get("source").isJsonNull()) {
        TrafficSource.validateJsonElement(jsonObj.get("source"));
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
       if (!OrderFields.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'OrderFields' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<OrderFields> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(OrderFields.class));

       return (TypeAdapter<T>) new TypeAdapter<OrderFields>() {
           @Override
           public void write(JsonWriter out, OrderFields value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public OrderFields read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of OrderFields given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of OrderFields
   * @throws IOException if the JSON string is invalid with respect to OrderFields
   */
  public static OrderFields fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, OrderFields.class);
  }

  /**
   * Convert an instance of OrderFields to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

