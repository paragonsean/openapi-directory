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
import org.openapitools.client.model.Id;

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
 * PromotionEditFields
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:37.537066-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class PromotionEditFields {
  public static final String SERIALIZED_NAME_BEGINS_AT = "begins_at";
  @SerializedName(SERIALIZED_NAME_BEGINS_AT)
  private String beginsAt;

  public static final String SERIALIZED_NAME_BUYS_AT_LEAST = "buys_at_least";
  @SerializedName(SERIALIZED_NAME_BUYS_AT_LEAST)
  private String buysAtLeast;

  public static final String SERIALIZED_NAME_CATEGORIES = "categories";
  @SerializedName(SERIALIZED_NAME_CATEGORIES)
  private List<Id> categories = new ArrayList<>();

  public static final String SERIALIZED_NAME_CODE = "code";
  @SerializedName(SERIALIZED_NAME_CODE)
  private String code;

  public static final String SERIALIZED_NAME_CONDITION_PRICE = "condition_price";
  @SerializedName(SERIALIZED_NAME_CONDITION_PRICE)
  private Float conditionPrice;

  public static final String SERIALIZED_NAME_CONDITION_QTY = "condition_qty";
  @SerializedName(SERIALIZED_NAME_CONDITION_QTY)
  private Integer conditionQty;

  public static final String SERIALIZED_NAME_CUMULATIVE = "cumulative";
  @SerializedName(SERIALIZED_NAME_CUMULATIVE)
  private Boolean cumulative = false;

  public static final String SERIALIZED_NAME_CUSTOMER_CATEGORIES = "customer_categories";
  @SerializedName(SERIALIZED_NAME_CUSTOMER_CATEGORIES)
  private List<Id> customerCategories = new ArrayList<>();

  public static final String SERIALIZED_NAME_CUSTOMERS = "customers";
  @SerializedName(SERIALIZED_NAME_CUSTOMERS)
  private String customers;

  public static final String SERIALIZED_NAME_DISCOUNT_AMOUNT_FIX = "discount_amount_fix";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_AMOUNT_FIX)
  private Float discountAmountFix;

  public static final String SERIALIZED_NAME_DISCOUNT_AMOUNT_PERCENT = "discount_amount_percent";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_AMOUNT_PERCENT)
  private Float discountAmountPercent;

  public static final String SERIALIZED_NAME_DISCOUNT_TARGET = "discount_target";
  @SerializedName(SERIALIZED_NAME_DISCOUNT_TARGET)
  private String discountTarget;

  public static final String SERIALIZED_NAME_ENABLED = "enabled";
  @SerializedName(SERIALIZED_NAME_ENABLED)
  private Boolean enabled = true;

  public static final String SERIALIZED_NAME_EXPIRES_AT = "expires_at";
  @SerializedName(SERIALIZED_NAME_EXPIRES_AT)
  private String expiresAt;

  public static final String SERIALIZED_NAME_LASTS = "lasts";
  @SerializedName(SERIALIZED_NAME_LASTS)
  private String lasts;

  public static final String SERIALIZED_NAME_MAX_TIMES_USED = "max_times_used";
  @SerializedName(SERIALIZED_NAME_MAX_TIMES_USED)
  private Integer maxTimesUsed;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PRODUCTS = "products";
  @SerializedName(SERIALIZED_NAME_PRODUCTS)
  private List<Id> products = new ArrayList<>();

  public static final String SERIALIZED_NAME_PRODUCTS_X = "products_x";
  @SerializedName(SERIALIZED_NAME_PRODUCTS_X)
  private List<Id> productsX = new ArrayList<>();

  public static final String SERIALIZED_NAME_QUANTITY_X = "quantity_x";
  @SerializedName(SERIALIZED_NAME_QUANTITY_X)
  private Integer quantityX;

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private String type;

  public PromotionEditFields() {
  }

  public PromotionEditFields beginsAt(String beginsAt) {
    this.beginsAt = beginsAt;
    return this;
  }

  /**
   * Creation date of the promotion (requires &#39;lasts&#39; param - &#39;date&#39;)
   * @return beginsAt
   */
  @javax.annotation.Nullable
  public String getBeginsAt() {
    return beginsAt;
  }

  public void setBeginsAt(String beginsAt) {
    this.beginsAt = beginsAt;
  }


  public PromotionEditFields buysAtLeast(String buysAtLeast) {
    this.buysAtLeast = buysAtLeast;
    return this;
  }

  /**
   * Controls the promotion&#39;s condition (&#39;none&#39;, &#39;price&#39;, &#39;qty&#39;)
   * @return buysAtLeast
   */
  @javax.annotation.Nullable
  public String getBuysAtLeast() {
    return buysAtLeast;
  }

  public void setBuysAtLeast(String buysAtLeast) {
    this.buysAtLeast = buysAtLeast;
  }


  public PromotionEditFields categories(List<Id> categories) {
    this.categories = categories;
    return this;
  }

  public PromotionEditFields addCategoriesItem(Id categoriesItem) {
    if (this.categories == null) {
      this.categories = new ArrayList<>();
    }
    this.categories.add(categoriesItem);
    return this;
  }

  /**
   * Products Categories where the promotion will be applied (requires &#39;discount_target&#39; param - &#39;categories&#39;)
   * @return categories
   */
  @javax.annotation.Nullable
  public List<Id> getCategories() {
    return categories;
  }

  public void setCategories(List<Id> categories) {
    this.categories = categories;
  }


  public PromotionEditFields code(String code) {
    this.code = code;
    return this;
  }

  /**
   * Code of the promotion
   * @return code
   */
  @javax.annotation.Nullable
  public String getCode() {
    return code;
  }

  public void setCode(String code) {
    this.code = code;
  }


  public PromotionEditFields conditionPrice(Float conditionPrice) {
    this.conditionPrice = conditionPrice;
    return this;
  }

  /**
   * Minimum order amount to validate the promotion (requires &#39;buys_at_least&#39; param - &#39;price&#39;)
   * @return conditionPrice
   */
  @javax.annotation.Nullable
  public Float getConditionPrice() {
    return conditionPrice;
  }

  public void setConditionPrice(Float conditionPrice) {
    this.conditionPrice = conditionPrice;
  }


  public PromotionEditFields conditionQty(Integer conditionQty) {
    this.conditionQty = conditionQty;
    return this;
  }

  /**
   * Minimum quantity of ordered itens to validate the promotion (requires &#39;buys_at_least&#39; param - &#39;qty&#39;)
   * @return conditionQty
   */
  @javax.annotation.Nullable
  public Integer getConditionQty() {
    return conditionQty;
  }

  public void setConditionQty(Integer conditionQty) {
    this.conditionQty = conditionQty;
  }


  public PromotionEditFields cumulative(Boolean cumulative) {
    this.cumulative = cumulative;
    return this;
  }

  /**
   * True if the promotion can be acumulated with others
   * @return cumulative
   */
  @javax.annotation.Nullable
  public Boolean getCumulative() {
    return cumulative;
  }

  public void setCumulative(Boolean cumulative) {
    this.cumulative = cumulative;
  }


  public PromotionEditFields customerCategories(List<Id> customerCategories) {
    this.customerCategories = customerCategories;
    return this;
  }

  public PromotionEditFields addCustomerCategoriesItem(Id customerCategoriesItem) {
    if (this.customerCategories == null) {
      this.customerCategories = new ArrayList<>();
    }
    this.customerCategories.add(customerCategoriesItem);
    return this;
  }

  /**
   * Customer Categories to whom the promotion will be applied (requires &#39;customers&#39; param - &#39;categories&#39;)
   * @return customerCategories
   */
  @javax.annotation.Nullable
  public List<Id> getCustomerCategories() {
    return customerCategories;
  }

  public void setCustomerCategories(List<Id> customerCategories) {
    this.customerCategories = customerCategories;
  }


  public PromotionEditFields customers(String customers) {
    this.customers = customers;
    return this;
  }

  /**
   * Controls to which customers the promotion will be applied (&#39;all&#39;, &#39;loggedin&#39;, &#39;categories&#39;, &#39;guests&#39;)
   * @return customers
   */
  @javax.annotation.Nullable
  public String getCustomers() {
    return customers;
  }

  public void setCustomers(String customers) {
    this.customers = customers;
  }


  public PromotionEditFields discountAmountFix(Float discountAmountFix) {
    this.discountAmountFix = discountAmountFix;
    return this;
  }

  /**
   * Fixed discount amount of the promotion (requires &#39;type&#39; param - &#39;fix&#39;)
   * @return discountAmountFix
   */
  @javax.annotation.Nullable
  public Float getDiscountAmountFix() {
    return discountAmountFix;
  }

  public void setDiscountAmountFix(Float discountAmountFix) {
    this.discountAmountFix = discountAmountFix;
  }


  public PromotionEditFields discountAmountPercent(Float discountAmountPercent) {
    this.discountAmountPercent = discountAmountPercent;
    return this;
  }

  /**
   * Percentual discount amount of the promotion (requires &#39;type&#39; param - &#39;percentage&#39;)
   * @return discountAmountPercent
   */
  @javax.annotation.Nullable
  public Float getDiscountAmountPercent() {
    return discountAmountPercent;
  }

  public void setDiscountAmountPercent(Float discountAmountPercent) {
    this.discountAmountPercent = discountAmountPercent;
  }


  public PromotionEditFields discountTarget(String discountTarget) {
    this.discountTarget = discountTarget;
    return this;
  }

  /**
   * Where the promotion will be applied (&#39;order&#39;, &#39;shipping&#39;, &#39;categories&#39;, &#39;buy_x_get_y)
   * @return discountTarget
   */
  @javax.annotation.Nullable
  public String getDiscountTarget() {
    return discountTarget;
  }

  public void setDiscountTarget(String discountTarget) {
    this.discountTarget = discountTarget;
  }


  public PromotionEditFields enabled(Boolean enabled) {
    this.enabled = enabled;
    return this;
  }

  /**
   * If the promotion is to be temporarily disabled
   * @return enabled
   */
  @javax.annotation.Nullable
  public Boolean getEnabled() {
    return enabled;
  }

  public void setEnabled(Boolean enabled) {
    this.enabled = enabled;
  }


  public PromotionEditFields expiresAt(String expiresAt) {
    this.expiresAt = expiresAt;
    return this;
  }

  /**
   * Expiration date of the promotion (requires &#39;lasts&#39; param - &#39;date&#39;)
   * @return expiresAt
   */
  @javax.annotation.Nullable
  public String getExpiresAt() {
    return expiresAt;
  }

  public void setExpiresAt(String expiresAt) {
    this.expiresAt = expiresAt;
  }


  public PromotionEditFields lasts(String lasts) {
    this.lasts = lasts;
    return this;
  }

  /**
   * Controls when the promotion will expire (&#39;none&#39;, &#39;date&#39;, &#39;max_times_used&#39;)
   * @return lasts
   */
  @javax.annotation.Nullable
  public String getLasts() {
    return lasts;
  }

  public void setLasts(String lasts) {
    this.lasts = lasts;
  }


  public PromotionEditFields maxTimesUsed(Integer maxTimesUsed) {
    this.maxTimesUsed = maxTimesUsed;
    return this;
  }

  /**
   * Maximum amount a promotion can be used (requires &#39;lasts&#39; param - &#39;max_times_used&#39;)
   * @return maxTimesUsed
   */
  @javax.annotation.Nullable
  public Integer getMaxTimesUsed() {
    return maxTimesUsed;
  }

  public void setMaxTimesUsed(Integer maxTimesUsed) {
    this.maxTimesUsed = maxTimesUsed;
  }


  public PromotionEditFields name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Name of the product
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public PromotionEditFields products(List<Id> products) {
    this.products = products;
    return this;
  }

  public PromotionEditFields addProductsItem(Id productsItem) {
    if (this.products == null) {
      this.products = new ArrayList<>();
    }
    this.products.add(productsItem);
    return this;
  }

  /**
   * Products where the promotion will be applied (requires &#39;discount_target&#39; param - &#39;categories&#39; or &#39;buy_x_get_y&#39;)
   * @return products
   */
  @javax.annotation.Nullable
  public List<Id> getProducts() {
    return products;
  }

  public void setProducts(List<Id> products) {
    this.products = products;
  }


  public PromotionEditFields productsX(List<Id> productsX) {
    this.productsX = productsX;
    return this;
  }

  public PromotionEditFields addProductsXItem(Id productsXItem) {
    if (this.productsX == null) {
      this.productsX = new ArrayList<>();
    }
    this.productsX.add(productsXItem);
    return this;
  }

  /**
   * Products required to apply the promotion (requires &#39;discount_target&#39; param - &#39;buy_x_get_y&#39;)
   * @return productsX
   */
  @javax.annotation.Nullable
  public List<Id> getProductsX() {
    return productsX;
  }

  public void setProductsX(List<Id> productsX) {
    this.productsX = productsX;
  }


  public PromotionEditFields quantityX(Integer quantityX) {
    this.quantityX = quantityX;
    return this;
  }

  /**
   * Number of sets of products_x needed to be able to apply the promotion (requires &#39;discount_target&#39; param - &#39;buy_x_get_y&#39;)
   * @return quantityX
   */
  @javax.annotation.Nullable
  public Integer getQuantityX() {
    return quantityX;
  }

  public void setQuantityX(Integer quantityX) {
    this.quantityX = quantityX;
  }


  public PromotionEditFields type(String type) {
    this.type = type;
    return this;
  }

  /**
   * Controls if the discount will be a fixed area (&#39;fix&#39;, &#39;percentage&#39;)
   * @return type
   */
  @javax.annotation.Nullable
  public String getType() {
    return type;
  }

  public void setType(String type) {
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
    PromotionEditFields promotionEditFields = (PromotionEditFields) o;
    return Objects.equals(this.beginsAt, promotionEditFields.beginsAt) &&
        Objects.equals(this.buysAtLeast, promotionEditFields.buysAtLeast) &&
        Objects.equals(this.categories, promotionEditFields.categories) &&
        Objects.equals(this.code, promotionEditFields.code) &&
        Objects.equals(this.conditionPrice, promotionEditFields.conditionPrice) &&
        Objects.equals(this.conditionQty, promotionEditFields.conditionQty) &&
        Objects.equals(this.cumulative, promotionEditFields.cumulative) &&
        Objects.equals(this.customerCategories, promotionEditFields.customerCategories) &&
        Objects.equals(this.customers, promotionEditFields.customers) &&
        Objects.equals(this.discountAmountFix, promotionEditFields.discountAmountFix) &&
        Objects.equals(this.discountAmountPercent, promotionEditFields.discountAmountPercent) &&
        Objects.equals(this.discountTarget, promotionEditFields.discountTarget) &&
        Objects.equals(this.enabled, promotionEditFields.enabled) &&
        Objects.equals(this.expiresAt, promotionEditFields.expiresAt) &&
        Objects.equals(this.lasts, promotionEditFields.lasts) &&
        Objects.equals(this.maxTimesUsed, promotionEditFields.maxTimesUsed) &&
        Objects.equals(this.name, promotionEditFields.name) &&
        Objects.equals(this.products, promotionEditFields.products) &&
        Objects.equals(this.productsX, promotionEditFields.productsX) &&
        Objects.equals(this.quantityX, promotionEditFields.quantityX) &&
        Objects.equals(this.type, promotionEditFields.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(beginsAt, buysAtLeast, categories, code, conditionPrice, conditionQty, cumulative, customerCategories, customers, discountAmountFix, discountAmountPercent, discountTarget, enabled, expiresAt, lasts, maxTimesUsed, name, products, productsX, quantityX, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PromotionEditFields {\n");
    sb.append("    beginsAt: ").append(toIndentedString(beginsAt)).append("\n");
    sb.append("    buysAtLeast: ").append(toIndentedString(buysAtLeast)).append("\n");
    sb.append("    categories: ").append(toIndentedString(categories)).append("\n");
    sb.append("    code: ").append(toIndentedString(code)).append("\n");
    sb.append("    conditionPrice: ").append(toIndentedString(conditionPrice)).append("\n");
    sb.append("    conditionQty: ").append(toIndentedString(conditionQty)).append("\n");
    sb.append("    cumulative: ").append(toIndentedString(cumulative)).append("\n");
    sb.append("    customerCategories: ").append(toIndentedString(customerCategories)).append("\n");
    sb.append("    customers: ").append(toIndentedString(customers)).append("\n");
    sb.append("    discountAmountFix: ").append(toIndentedString(discountAmountFix)).append("\n");
    sb.append("    discountAmountPercent: ").append(toIndentedString(discountAmountPercent)).append("\n");
    sb.append("    discountTarget: ").append(toIndentedString(discountTarget)).append("\n");
    sb.append("    enabled: ").append(toIndentedString(enabled)).append("\n");
    sb.append("    expiresAt: ").append(toIndentedString(expiresAt)).append("\n");
    sb.append("    lasts: ").append(toIndentedString(lasts)).append("\n");
    sb.append("    maxTimesUsed: ").append(toIndentedString(maxTimesUsed)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    products: ").append(toIndentedString(products)).append("\n");
    sb.append("    productsX: ").append(toIndentedString(productsX)).append("\n");
    sb.append("    quantityX: ").append(toIndentedString(quantityX)).append("\n");
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
    openapiFields.add("begins_at");
    openapiFields.add("buys_at_least");
    openapiFields.add("categories");
    openapiFields.add("code");
    openapiFields.add("condition_price");
    openapiFields.add("condition_qty");
    openapiFields.add("cumulative");
    openapiFields.add("customer_categories");
    openapiFields.add("customers");
    openapiFields.add("discount_amount_fix");
    openapiFields.add("discount_amount_percent");
    openapiFields.add("discount_target");
    openapiFields.add("enabled");
    openapiFields.add("expires_at");
    openapiFields.add("lasts");
    openapiFields.add("max_times_used");
    openapiFields.add("name");
    openapiFields.add("products");
    openapiFields.add("products_x");
    openapiFields.add("quantity_x");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to PromotionEditFields
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!PromotionEditFields.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in PromotionEditFields is not found in the empty JSON string", PromotionEditFields.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!PromotionEditFields.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `PromotionEditFields` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("begins_at") != null && !jsonObj.get("begins_at").isJsonNull()) && !jsonObj.get("begins_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `begins_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("begins_at").toString()));
      }
      if ((jsonObj.get("buys_at_least") != null && !jsonObj.get("buys_at_least").isJsonNull()) && !jsonObj.get("buys_at_least").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `buys_at_least` to be a primitive type in the JSON string but got `%s`", jsonObj.get("buys_at_least").toString()));
      }
      if (jsonObj.get("categories") != null && !jsonObj.get("categories").isJsonNull()) {
        JsonArray jsonArraycategories = jsonObj.getAsJsonArray("categories");
        if (jsonArraycategories != null) {
          // ensure the json data is an array
          if (!jsonObj.get("categories").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `categories` to be an array in the JSON string but got `%s`", jsonObj.get("categories").toString()));
          }

          // validate the optional field `categories` (array)
          for (int i = 0; i < jsonArraycategories.size(); i++) {
            Id.validateJsonElement(jsonArraycategories.get(i));
          };
        }
      }
      if ((jsonObj.get("code") != null && !jsonObj.get("code").isJsonNull()) && !jsonObj.get("code").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `code` to be a primitive type in the JSON string but got `%s`", jsonObj.get("code").toString()));
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
            Id.validateJsonElement(jsonArraycustomerCategories.get(i));
          };
        }
      }
      if ((jsonObj.get("customers") != null && !jsonObj.get("customers").isJsonNull()) && !jsonObj.get("customers").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `customers` to be a primitive type in the JSON string but got `%s`", jsonObj.get("customers").toString()));
      }
      if ((jsonObj.get("discount_target") != null && !jsonObj.get("discount_target").isJsonNull()) && !jsonObj.get("discount_target").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `discount_target` to be a primitive type in the JSON string but got `%s`", jsonObj.get("discount_target").toString()));
      }
      if ((jsonObj.get("expires_at") != null && !jsonObj.get("expires_at").isJsonNull()) && !jsonObj.get("expires_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `expires_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("expires_at").toString()));
      }
      if ((jsonObj.get("lasts") != null && !jsonObj.get("lasts").isJsonNull()) && !jsonObj.get("lasts").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `lasts` to be a primitive type in the JSON string but got `%s`", jsonObj.get("lasts").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
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
            Id.validateJsonElement(jsonArrayproducts.get(i));
          };
        }
      }
      if (jsonObj.get("products_x") != null && !jsonObj.get("products_x").isJsonNull()) {
        JsonArray jsonArrayproductsX = jsonObj.getAsJsonArray("products_x");
        if (jsonArrayproductsX != null) {
          // ensure the json data is an array
          if (!jsonObj.get("products_x").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `products_x` to be an array in the JSON string but got `%s`", jsonObj.get("products_x").toString()));
          }

          // validate the optional field `products_x` (array)
          for (int i = 0; i < jsonArrayproductsX.size(); i++) {
            Id.validateJsonElement(jsonArrayproductsX.get(i));
          };
        }
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!PromotionEditFields.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'PromotionEditFields' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<PromotionEditFields> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(PromotionEditFields.class));

       return (TypeAdapter<T>) new TypeAdapter<PromotionEditFields>() {
           @Override
           public void write(JsonWriter out, PromotionEditFields value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public PromotionEditFields read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of PromotionEditFields given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of PromotionEditFields
   * @throws IOException if the JSON string is invalid with respect to PromotionEditFields
   */
  public static PromotionEditFields fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, PromotionEditFields.class);
  }

  /**
   * Convert an instance of PromotionEditFields to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

