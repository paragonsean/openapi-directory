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
import org.openapitools.client.model.CategoryFields;
import org.openapitools.client.model.ImageFields;
import org.openapitools.client.model.VariantFields;

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
 * ProductFields
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:31:37.537066-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ProductFields {
  public static final String SERIALIZED_NAME_BARCODE = "barcode";
  @SerializedName(SERIALIZED_NAME_BARCODE)
  private String barcode;

  public static final String SERIALIZED_NAME_CATEGORIES = "categories";
  @SerializedName(SERIALIZED_NAME_CATEGORIES)
  private List<CategoryFields> categories = new ArrayList<>();

  public static final String SERIALIZED_NAME_CREATED_AT = "created_at";
  @SerializedName(SERIALIZED_NAME_CREATED_AT)
  private String createdAt;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_DIAMETER = "diameter";
  @SerializedName(SERIALIZED_NAME_DIAMETER)
  private Float diameter;

  public static final String SERIALIZED_NAME_DISCOUNT = "discount";
  @SerializedName(SERIALIZED_NAME_DISCOUNT)
  private Float discount;

  public static final String SERIALIZED_NAME_FEATURED = "featured";
  @SerializedName(SERIALIZED_NAME_FEATURED)
  private Boolean featured = false;

  public static final String SERIALIZED_NAME_GOOGLE_PRODUCT_CATEGORY = "google_product_category";
  @SerializedName(SERIALIZED_NAME_GOOGLE_PRODUCT_CATEGORY)
  private String googleProductCategory;

  public static final String SERIALIZED_NAME_HEIGHT = "height";
  @SerializedName(SERIALIZED_NAME_HEIGHT)
  private Float height;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private Integer id;

  public static final String SERIALIZED_NAME_IMAGES = "images";
  @SerializedName(SERIALIZED_NAME_IMAGES)
  private List<ImageFields> images = new ArrayList<>();

  public static final String SERIALIZED_NAME_LENGTH = "length";
  @SerializedName(SERIALIZED_NAME_LENGTH)
  private Float length;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  /**
   * Format the product package
   */
  @JsonAdapter(PackageFormatEnum.Adapter.class)
  public enum PackageFormatEnum {
    BOX("box"),
    
    CYLINDER("cylinder");

    private String value;

    PackageFormatEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static PackageFormatEnum fromValue(String value) {
      for (PackageFormatEnum b : PackageFormatEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<PackageFormatEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final PackageFormatEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public PackageFormatEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return PackageFormatEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      PackageFormatEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_PACKAGE_FORMAT = "package_format";
  @SerializedName(SERIALIZED_NAME_PACKAGE_FORMAT)
  private PackageFormatEnum packageFormat = PackageFormatEnum.BOX;

  public static final String SERIALIZED_NAME_PERMALINK = "permalink";
  @SerializedName(SERIALIZED_NAME_PERMALINK)
  private String permalink;

  public static final String SERIALIZED_NAME_PRICE = "price";
  @SerializedName(SERIALIZED_NAME_PRICE)
  private Float price;

  public static final String SERIALIZED_NAME_SKU = "sku";
  @SerializedName(SERIALIZED_NAME_SKU)
  private String sku;

  /**
   * Status of the product
   */
  @JsonAdapter(StatusEnum.Adapter.class)
  public enum StatusEnum {
    AVAILABLE("available"),
    
    NOT_AVAILABLE("not-available"),
    
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
  private StatusEnum status = StatusEnum.AVAILABLE;

  public static final String SERIALIZED_NAME_STOCK = "stock";
  @SerializedName(SERIALIZED_NAME_STOCK)
  private Integer stock = 100;

  public static final String SERIALIZED_NAME_STOCK_UNLIMITED = "stock_unlimited";
  @SerializedName(SERIALIZED_NAME_STOCK_UNLIMITED)
  private Boolean stockUnlimited;

  public static final String SERIALIZED_NAME_VARIANTS = "variants";
  @SerializedName(SERIALIZED_NAME_VARIANTS)
  private List<VariantFields> variants = new ArrayList<>();

  public static final String SERIALIZED_NAME_WEIGHT = "weight";
  @SerializedName(SERIALIZED_NAME_WEIGHT)
  private Float weight = 1f;

  public static final String SERIALIZED_NAME_WIDTH = "width";
  @SerializedName(SERIALIZED_NAME_WIDTH)
  private Float width;

  public ProductFields() {
  }

  public ProductFields barcode(String barcode) {
    this.barcode = barcode;
    return this;
  }

  /**
   * Barcode of the product
   * @return barcode
   */
  @javax.annotation.Nullable
  public String getBarcode() {
    return barcode;
  }

  public void setBarcode(String barcode) {
    this.barcode = barcode;
  }


  public ProductFields categories(List<CategoryFields> categories) {
    this.categories = categories;
    return this;
  }

  public ProductFields addCategoriesItem(CategoryFields categoriesItem) {
    if (this.categories == null) {
      this.categories = new ArrayList<>();
    }
    this.categories.add(categoriesItem);
    return this;
  }

  /**
   * Get categories
   * @return categories
   */
  @javax.annotation.Nullable
  public List<CategoryFields> getCategories() {
    return categories;
  }

  public void setCategories(List<CategoryFields> categories) {
    this.categories = categories;
  }


  public ProductFields createdAt(String createdAt) {
    this.createdAt = createdAt;
    return this;
  }

  /**
   * Date of product creation
   * @return createdAt
   */
  @javax.annotation.Nullable
  public String getCreatedAt() {
    return createdAt;
  }

  public void setCreatedAt(String createdAt) {
    this.createdAt = createdAt;
  }


  public ProductFields description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Description of the product
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public ProductFields diameter(Float diameter) {
    this.diameter = diameter;
    return this;
  }

  /**
   * Diameter of the product
   * @return diameter
   */
  @javax.annotation.Nullable
  public Float getDiameter() {
    return diameter;
  }

  public void setDiameter(Float diameter) {
    this.diameter = diameter;
  }


  public ProductFields discount(Float discount) {
    this.discount = discount;
    return this;
  }

  /**
   * Discount of the product
   * @return discount
   */
  @javax.annotation.Nullable
  public Float getDiscount() {
    return discount;
  }

  public void setDiscount(Float discount) {
    this.discount = discount;
  }


  public ProductFields featured(Boolean featured) {
    this.featured = featured;
    return this;
  }

  /**
   * True if the product is featured
   * @return featured
   */
  @javax.annotation.Nullable
  public Boolean getFeatured() {
    return featured;
  }

  public void setFeatured(Boolean featured) {
    this.featured = featured;
  }


  public ProductFields googleProductCategory(String googleProductCategory) {
    this.googleProductCategory = googleProductCategory;
    return this;
  }

  /**
   * Category of a Product based on the Google product taxonomy
   * @return googleProductCategory
   */
  @javax.annotation.Nullable
  public String getGoogleProductCategory() {
    return googleProductCategory;
  }

  public void setGoogleProductCategory(String googleProductCategory) {
    this.googleProductCategory = googleProductCategory;
  }


  public ProductFields height(Float height) {
    this.height = height;
    return this;
  }

  /**
   * Height of the product
   * @return height
   */
  @javax.annotation.Nullable
  public Float getHeight() {
    return height;
  }

  public void setHeight(Float height) {
    this.height = height;
  }


  public ProductFields id(Integer id) {
    this.id = id;
    return this;
  }

  /**
   * Unique identifier of the product
   * @return id
   */
  @javax.annotation.Nullable
  public Integer getId() {
    return id;
  }

  public void setId(Integer id) {
    this.id = id;
  }


  public ProductFields images(List<ImageFields> images) {
    this.images = images;
    return this;
  }

  public ProductFields addImagesItem(ImageFields imagesItem) {
    if (this.images == null) {
      this.images = new ArrayList<>();
    }
    this.images.add(imagesItem);
    return this;
  }

  /**
   * Get images
   * @return images
   */
  @javax.annotation.Nullable
  public List<ImageFields> getImages() {
    return images;
  }

  public void setImages(List<ImageFields> images) {
    this.images = images;
  }


  public ProductFields length(Float length) {
    this.length = length;
    return this;
  }

  /**
   * Length of the product
   * @return length
   */
  @javax.annotation.Nullable
  public Float getLength() {
    return length;
  }

  public void setLength(Float length) {
    this.length = length;
  }


  public ProductFields name(String name) {
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


  public ProductFields packageFormat(PackageFormatEnum packageFormat) {
    this.packageFormat = packageFormat;
    return this;
  }

  /**
   * Format the product package
   * @return packageFormat
   */
  @javax.annotation.Nullable
  public PackageFormatEnum getPackageFormat() {
    return packageFormat;
  }

  public void setPackageFormat(PackageFormatEnum packageFormat) {
    this.packageFormat = packageFormat;
  }


  public ProductFields permalink(String permalink) {
    this.permalink = permalink;
    return this;
  }

  /**
   * Product unique URL path
   * @return permalink
   */
  @javax.annotation.Nullable
  public String getPermalink() {
    return permalink;
  }

  public void setPermalink(String permalink) {
    this.permalink = permalink;
  }


  public ProductFields price(Float price) {
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


  public ProductFields sku(String sku) {
    this.sku = sku;
    return this;
  }

  /**
   * Stock Keeping Unit of the product
   * @return sku
   */
  @javax.annotation.Nullable
  public String getSku() {
    return sku;
  }

  public void setSku(String sku) {
    this.sku = sku;
  }


  public ProductFields status(StatusEnum status) {
    this.status = status;
    return this;
  }

  /**
   * Status of the product
   * @return status
   */
  @javax.annotation.Nullable
  public StatusEnum getStatus() {
    return status;
  }

  public void setStatus(StatusEnum status) {
    this.status = status;
  }


  public ProductFields stock(Integer stock) {
    this.stock = stock;
    return this;
  }

  /**
   * Quantity in stock for the product
   * @return stock
   */
  @javax.annotation.Nullable
  public Integer getStock() {
    return stock;
  }

  public void setStock(Integer stock) {
    this.stock = stock;
  }


  public ProductFields stockUnlimited(Boolean stockUnlimited) {
    this.stockUnlimited = stockUnlimited;
    return this;
  }

  /**
   * True if the Product has unlimited stock
   * @return stockUnlimited
   */
  @javax.annotation.Nullable
  public Boolean getStockUnlimited() {
    return stockUnlimited;
  }

  public void setStockUnlimited(Boolean stockUnlimited) {
    this.stockUnlimited = stockUnlimited;
  }


  public ProductFields variants(List<VariantFields> variants) {
    this.variants = variants;
    return this;
  }

  public ProductFields addVariantsItem(VariantFields variantsItem) {
    if (this.variants == null) {
      this.variants = new ArrayList<>();
    }
    this.variants.add(variantsItem);
    return this;
  }

  /**
   * Get variants
   * @return variants
   */
  @javax.annotation.Nullable
  public List<VariantFields> getVariants() {
    return variants;
  }

  public void setVariants(List<VariantFields> variants) {
    this.variants = variants;
  }


  public ProductFields weight(Float weight) {
    this.weight = weight;
    return this;
  }

  /**
   * Weight of the product
   * @return weight
   */
  @javax.annotation.Nullable
  public Float getWeight() {
    return weight;
  }

  public void setWeight(Float weight) {
    this.weight = weight;
  }


  public ProductFields width(Float width) {
    this.width = width;
    return this;
  }

  /**
   * Width of the product
   * @return width
   */
  @javax.annotation.Nullable
  public Float getWidth() {
    return width;
  }

  public void setWidth(Float width) {
    this.width = width;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ProductFields productFields = (ProductFields) o;
    return Objects.equals(this.barcode, productFields.barcode) &&
        Objects.equals(this.categories, productFields.categories) &&
        Objects.equals(this.createdAt, productFields.createdAt) &&
        Objects.equals(this.description, productFields.description) &&
        Objects.equals(this.diameter, productFields.diameter) &&
        Objects.equals(this.discount, productFields.discount) &&
        Objects.equals(this.featured, productFields.featured) &&
        Objects.equals(this.googleProductCategory, productFields.googleProductCategory) &&
        Objects.equals(this.height, productFields.height) &&
        Objects.equals(this.id, productFields.id) &&
        Objects.equals(this.images, productFields.images) &&
        Objects.equals(this.length, productFields.length) &&
        Objects.equals(this.name, productFields.name) &&
        Objects.equals(this.packageFormat, productFields.packageFormat) &&
        Objects.equals(this.permalink, productFields.permalink) &&
        Objects.equals(this.price, productFields.price) &&
        Objects.equals(this.sku, productFields.sku) &&
        Objects.equals(this.status, productFields.status) &&
        Objects.equals(this.stock, productFields.stock) &&
        Objects.equals(this.stockUnlimited, productFields.stockUnlimited) &&
        Objects.equals(this.variants, productFields.variants) &&
        Objects.equals(this.weight, productFields.weight) &&
        Objects.equals(this.width, productFields.width);
  }

  @Override
  public int hashCode() {
    return Objects.hash(barcode, categories, createdAt, description, diameter, discount, featured, googleProductCategory, height, id, images, length, name, packageFormat, permalink, price, sku, status, stock, stockUnlimited, variants, weight, width);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ProductFields {\n");
    sb.append("    barcode: ").append(toIndentedString(barcode)).append("\n");
    sb.append("    categories: ").append(toIndentedString(categories)).append("\n");
    sb.append("    createdAt: ").append(toIndentedString(createdAt)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    diameter: ").append(toIndentedString(diameter)).append("\n");
    sb.append("    discount: ").append(toIndentedString(discount)).append("\n");
    sb.append("    featured: ").append(toIndentedString(featured)).append("\n");
    sb.append("    googleProductCategory: ").append(toIndentedString(googleProductCategory)).append("\n");
    sb.append("    height: ").append(toIndentedString(height)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    images: ").append(toIndentedString(images)).append("\n");
    sb.append("    length: ").append(toIndentedString(length)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    packageFormat: ").append(toIndentedString(packageFormat)).append("\n");
    sb.append("    permalink: ").append(toIndentedString(permalink)).append("\n");
    sb.append("    price: ").append(toIndentedString(price)).append("\n");
    sb.append("    sku: ").append(toIndentedString(sku)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    stock: ").append(toIndentedString(stock)).append("\n");
    sb.append("    stockUnlimited: ").append(toIndentedString(stockUnlimited)).append("\n");
    sb.append("    variants: ").append(toIndentedString(variants)).append("\n");
    sb.append("    weight: ").append(toIndentedString(weight)).append("\n");
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
    openapiFields.add("barcode");
    openapiFields.add("categories");
    openapiFields.add("created_at");
    openapiFields.add("description");
    openapiFields.add("diameter");
    openapiFields.add("discount");
    openapiFields.add("featured");
    openapiFields.add("google_product_category");
    openapiFields.add("height");
    openapiFields.add("id");
    openapiFields.add("images");
    openapiFields.add("length");
    openapiFields.add("name");
    openapiFields.add("package_format");
    openapiFields.add("permalink");
    openapiFields.add("price");
    openapiFields.add("sku");
    openapiFields.add("status");
    openapiFields.add("stock");
    openapiFields.add("stock_unlimited");
    openapiFields.add("variants");
    openapiFields.add("weight");
    openapiFields.add("width");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ProductFields
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ProductFields.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ProductFields is not found in the empty JSON string", ProductFields.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ProductFields.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ProductFields` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("barcode") != null && !jsonObj.get("barcode").isJsonNull()) && !jsonObj.get("barcode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `barcode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("barcode").toString()));
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
            CategoryFields.validateJsonElement(jsonArraycategories.get(i));
          };
        }
      }
      if ((jsonObj.get("created_at") != null && !jsonObj.get("created_at").isJsonNull()) && !jsonObj.get("created_at").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_at` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_at").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("google_product_category") != null && !jsonObj.get("google_product_category").isJsonNull()) && !jsonObj.get("google_product_category").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `google_product_category` to be a primitive type in the JSON string but got `%s`", jsonObj.get("google_product_category").toString()));
      }
      if (jsonObj.get("images") != null && !jsonObj.get("images").isJsonNull()) {
        JsonArray jsonArrayimages = jsonObj.getAsJsonArray("images");
        if (jsonArrayimages != null) {
          // ensure the json data is an array
          if (!jsonObj.get("images").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `images` to be an array in the JSON string but got `%s`", jsonObj.get("images").toString()));
          }

          // validate the optional field `images` (array)
          for (int i = 0; i < jsonArrayimages.size(); i++) {
            ImageFields.validateJsonElement(jsonArrayimages.get(i));
          };
        }
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("package_format") != null && !jsonObj.get("package_format").isJsonNull()) && !jsonObj.get("package_format").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `package_format` to be a primitive type in the JSON string but got `%s`", jsonObj.get("package_format").toString()));
      }
      // validate the optional field `package_format`
      if (jsonObj.get("package_format") != null && !jsonObj.get("package_format").isJsonNull()) {
        PackageFormatEnum.validateJsonElement(jsonObj.get("package_format"));
      }
      if ((jsonObj.get("permalink") != null && !jsonObj.get("permalink").isJsonNull()) && !jsonObj.get("permalink").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `permalink` to be a primitive type in the JSON string but got `%s`", jsonObj.get("permalink").toString()));
      }
      if ((jsonObj.get("sku") != null && !jsonObj.get("sku").isJsonNull()) && !jsonObj.get("sku").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `sku` to be a primitive type in the JSON string but got `%s`", jsonObj.get("sku").toString()));
      }
      if ((jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) && !jsonObj.get("status").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `status` to be a primitive type in the JSON string but got `%s`", jsonObj.get("status").toString()));
      }
      // validate the optional field `status`
      if (jsonObj.get("status") != null && !jsonObj.get("status").isJsonNull()) {
        StatusEnum.validateJsonElement(jsonObj.get("status"));
      }
      if (jsonObj.get("variants") != null && !jsonObj.get("variants").isJsonNull()) {
        JsonArray jsonArrayvariants = jsonObj.getAsJsonArray("variants");
        if (jsonArrayvariants != null) {
          // ensure the json data is an array
          if (!jsonObj.get("variants").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `variants` to be an array in the JSON string but got `%s`", jsonObj.get("variants").toString()));
          }

          // validate the optional field `variants` (array)
          for (int i = 0; i < jsonArrayvariants.size(); i++) {
            VariantFields.validateJsonElement(jsonArrayvariants.get(i));
          };
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ProductFields.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ProductFields' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ProductFields> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ProductFields.class));

       return (TypeAdapter<T>) new TypeAdapter<ProductFields>() {
           @Override
           public void write(JsonWriter out, ProductFields value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ProductFields read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ProductFields given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ProductFields
   * @throws IOException if the JSON string is invalid with respect to ProductFields
   */
  public static ProductFields fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ProductFields.class);
  }

  /**
   * Convert an instance of ProductFields to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

