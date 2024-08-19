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
import org.openapitools.client.model.ProductOptionVariantEdit;

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
 * VariantEditFields
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:37.537066-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class VariantEditFields {
  public static final String SERIALIZED_NAME_IMAGE_ID = "image_id";
  @SerializedName(SERIALIZED_NAME_IMAGE_ID)
  private Integer imageId;

  public static final String SERIALIZED_NAME_OPTIONS = "options";
  @SerializedName(SERIALIZED_NAME_OPTIONS)
  private List<ProductOptionVariantEdit> options = new ArrayList<>();

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private Float price;

  public static final String SERIALIZED_NAME_SKU = "sku";
  @SerializedName(SERIALIZED_NAME_SKU)
  private String sku;

  public static final String SERIALIZED_NAME_STOCK = "stock";
  @SerializedName(SERIALIZED_NAME_STOCK)
  private Integer stock = 100;

  public static final String SERIALIZED_NAME_STOCK_UNLIMITED = "stock_unlimited";
  @SerializedName(SERIALIZED_NAME_STOCK_UNLIMITED)
  private Boolean stockUnlimited;

  public VariantEditFields() {
  }

  public VariantEditFields imageId(Integer imageId) {
    this.imageId = imageId;
    return this;
  }

  /**
   * Unique identifier of the product image to associate with this variant
   * @return imageId
   */
  @javax.annotation.Nullable
  public Integer getImageId() {
    return imageId;
  }

  public void setImageId(Integer imageId) {
    this.imageId = imageId;
  }


  public VariantEditFields options(List<ProductOptionVariantEdit> options) {
    this.options = options;
    return this;
  }

  public VariantEditFields addOptionsItem(ProductOptionVariantEdit optionsItem) {
    if (this.options == null) {
      this.options = new ArrayList<>();
    }
    this.options.add(optionsItem);
    return this;
  }

  /**
   * Get options
   * @return options
   */
  @javax.annotation.Nullable
  public List<ProductOptionVariantEdit> getOptions() {
    return options;
  }

  public void setOptions(List<ProductOptionVariantEdit> options) {
    this.options = options;
  }


  public VariantEditFields price(Float price) {
    this.price = price;
    return this;
  }

  /**
   * Price of the product
   * @return price
   */
  @javax.annotation.Nullable
  public Float getPrice() {
    return price;
  }

  public void setPrice(Float price) {
    this.price = price;
  }


  public VariantEditFields sku(String sku) {
    this.sku = sku;
    return this;
  }

  /**
   * Stock Keeping Unit of the Product&#39;s Variant
   * @return sku
   */
  @javax.annotation.Nullable
  public String getSku() {
    return sku;
  }

  public void setSku(String sku) {
    this.sku = sku;
  }


  public VariantEditFields stock(Integer stock) {
    this.stock = stock;
    return this;
  }

  /**
   * Quantity in stock for the Product&#39;s Variant
   * @return stock
   */
  @javax.annotation.Nullable
  public Integer getStock() {
    return stock;
  }

  public void setStock(Integer stock) {
    this.stock = stock;
  }


  public VariantEditFields stockUnlimited(Boolean stockUnlimited) {
    this.stockUnlimited = stockUnlimited;
    return this;
  }

  /**
   * True if the Product&#39;s Variant has unlimited stock
   * @return stockUnlimited
   */
  @javax.annotation.Nullable
  public Boolean getStockUnlimited() {
    return stockUnlimited;
  }

  public void setStockUnlimited(Boolean stockUnlimited) {
    this.stockUnlimited = stockUnlimited;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VariantEditFields variantEditFields = (VariantEditFields) o;
    return Objects.equals(this.imageId, variantEditFields.imageId) &&
        Objects.equals(this.options, variantEditFields.options) &&
        Objects.equals(this.price, variantEditFields.price) &&
        Objects.equals(this.sku, variantEditFields.sku) &&
        Objects.equals(this.stock, variantEditFields.stock) &&
        Objects.equals(this.stockUnlimited, variantEditFields.stockUnlimited);
  }

  @Override
  public int hashCode() {
    return Objects.hash(imageId, options, price, sku, stock, stockUnlimited);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VariantEditFields {\n");
    sb.append("    imageId: ").append(toIndentedString(imageId)).append("\n");
    sb.append("    options: ").append(toIndentedString(options)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    sku: ").append(toIndentedString(sku)).append("\n");
    sb.append("    stock: ").append(toIndentedString(stock)).append("\n");
    sb.append("    stockUnlimited: ").append(toIndentedString(stockUnlimited)).append("\n");
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
    openapiFields.add("image_id");
    openapiFields.add("options");
    openapiFields.add("price");
    openapiFields.add("sku");
    openapiFields.add("stock");
    openapiFields.add("stock_unlimited");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to VariantEditFields
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!VariantEditFields.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in VariantEditFields is not found in the empty JSON string", VariantEditFields.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!VariantEditFields.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `VariantEditFields` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("options") != null && !jsonObj.get("options").isJsonNull()) {
        JsonArray jsonArrayoptions = jsonObj.getAsJsonArray("options");
        if (jsonArrayoptions != null) {
          // ensure the json data is an array
          if (!jsonObj.get("options").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `options` to be an array in the JSON string but got `%s`", jsonObj.get("options").toString()));
          }

          // validate the optional field `options` (array)
          for (int i = 0; i < jsonArrayoptions.size(); i++) {
            ProductOptionVariantEdit.validateJsonElement(jsonArrayoptions.get(i));
          };
        }
      }
      if ((jsonObj.get("sku") != null && !jsonObj.get("sku").isJsonNull()) && !jsonObj.get("sku").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sku` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sku").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!VariantEditFields.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'VariantEditFields' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<VariantEditFields> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(VariantEditFields.class));

       return (TypeAdapter<T>) new TypeAdapter<VariantEditFields>() {
           @Override
           public void write(JsonWriter out, VariantEditFields value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public VariantEditFields read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of VariantEditFields given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of VariantEditFields
   * @throws IOException if the JSON string is invalid with respect to VariantEditFields
   */
  public static VariantEditFields fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, VariantEditFields.class);
  }

  /**
   * Convert an instance of VariantEditFields to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

