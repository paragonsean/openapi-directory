/*
 * Apacta
 * API for a tool to craftsmen used to register working hours, material usage and quality assurance. # Endpoint The endpoint `https://app.apacta.com/api/v1` should be used to communicate with the API. API access is only allowed with SSL encrypted connection (https). # Authentication URL query authentication with an API key is used, so appending `?api_key={api_key}` to the URL where `{api_key}` is found within Apacta settings is used for authentication # Pagination If the endpoint returns a `pagination` object it means the endpoint supports pagination - currently it's only possible to change pages with `?page={page_number}` but implementing custom page sizes are on the road map.   # Search/filter Is experimental but implemented in some cases - see the individual endpoints' docs for further explanation. # Ordering Is currently experimental, but on some endpoints it's implemented on URL querys so eg. to order Invoices by `invoice_number` appending `?sort=Invoices.invoice_number&direction=desc` would sort the list descending by the value of `invoice_number`. # Associations Is currently implemented on an experimental basis where you can append eg. `?include=Contacts,Projects`  to the `/api/v1/invoices/` endpoint to embed `Contact` and `Project` objects directly. # Project Files Currently project files can be retrieved from two endpoints. `/projects/{project_id}/files` handles files uploaded from wall posts or forms. `/projects/{project_id}/project_files` allows uploading and showing files, not belonging to specific form or wall post. # Errors/Exceptions ## 422 (Validation) Write something about how the `errors` object contains keys with the properties that failes validation like: ```   {       \"success\": false,       \"data\": {           \"code\": 422,           \"url\": \"/api/v1/contacts?api_key=5523be3b-30ef-425d-8203-04df7caaa93a\",           \"message\": \"A validation error occurred\",           \"errorCount\": 1,           \"errors\": {               \"contact_types\": [ ## Property name that failed validation                   \"Contacts must have at least one contact type\" ## Message with further explanation               ]           }       }   } ``` ## Code examples Running examples of how to retrieve the 5 most recent forms registered and embed the details of the User that made the form, and eventual products contained in the form ### Swift ``` ``` ### Java #### OkHttp ```   OkHttpClient client = new OkHttpClient();    Request request = new Request.Builder()     .url(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .get()     .addHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .addHeader(\"accept\", \"application/json\")     .build();    Response response = client.newCall(request).execute(); ``` #### Unirest ```   HttpResponse<String> response = Unirest.get(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")     .header(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\")     .header(\"accept\", \"application/json\")     .asString(); ``` ### Javascript #### Native ```   var data = null;    var xhr = new XMLHttpRequest();    xhr.addEventListener(\"readystatechange\", function () {     if (this.readyState === 4) {       console.log(this.responseText);     }   });    xhr.open(\"GET\", \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   xhr.setRequestHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   xhr.setRequestHeader(\"accept\", \"application/json\");    xhr.send(data); ``` #### jQuery ```   var settings = {     \"async\": true,     \"crossDomain\": true,     \"url\": \"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\",     \"method\": \"GET\",     \"headers\": {       \"x-auth-token\": \"{INSERT_YOUR_TOKEN}\",       \"accept\": \"application/json\",     }   }    $.ajax(settings).done(function (response) {     console.log(response);   }); ``` #### NodeJS (Request) ```   var request = require(\"request\");    var options = { method: 'GET',     url: 'https://app.apacta.com/api/v1/forms',     qs:      { extended: 'true',        sort: 'Forms.created',        direction: 'DESC',        include: 'Products,CreatedBy',        limit: '5' },     headers:      { accept: 'application/json',        'x-auth-token': '{INSERT_YOUR_TOKEN}' } };    request(options, function (error, response, body) {     if (error) throw new Error(error);      console.log(body);   });  ``` ### Python 3 ```   import http.client    conn = http.client.HTTPSConnection(\"app.apacta.com\")    payload = \"\"    headers = {       'x-auth-token': \"{INSERT_YOUR_TOKEN}\",       'accept': \"application/json\",       }    conn.request(\"GET\", \"/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\", payload, headers)    res = conn.getresponse()   data = res.read()    print(data.decode(\"utf-8\")) ``` ### C# #### RestSharp ```   var client = new RestClient(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\");   var request = new RestRequest(Method.GET);   request.AddHeader(\"accept\", \"application/json\");   request.AddHeader(\"x-auth-token\", \"{INSERT_YOUR_TOKEN}\");   IRestResponse response = client.Execute(request); ``` ### Ruby ```   require 'uri'   require 'net/http'    url = URI(\"https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5\")    http = Net::HTTP.new(url.host, url.port)   http.use_ssl = true   http.verify_mode = OpenSSL::SSL::VERIFY_NONE    request = Net::HTTP::Get.new(url)   request[\"x-auth-token\"] = '{INSERT_YOUR_TOKEN}'   request[\"accept\"] = 'application/json'    response = http.request(request)   puts response.read_body ``` ### PHP (HttpRequest) ```   <?php    $request = new HttpRequest();   $request->setUrl('https://app.apacta.com/api/v1/forms');   $request->setMethod(HTTP_METH_GET);    $request->setQueryData(array(     'extended' => 'true',     'sort' => 'Forms.created',     'direction' => 'DESC',     'include' => 'Products,CreatedBy',     'limit' => '5'   ));    $request->setHeaders(array(     'accept' => 'application/json',     'x-auth-token' => '{INSERT_YOUR_TOKEN}'   ));    try {     $response = $request->send();      echo $response->getBody();   } catch (HttpException $ex) {     echo $ex;   } ``` ### Shell (cURL) ```    $ curl --request GET --url 'https://app.apacta.com/api/v1/forms?extended=true&sort=Forms.created&direction=DESC&include=Products%2CCreatedBy&limit=5' --header 'accept: application/json' --header 'x-auth-token: {INSERT_YOUR_TOKEN}'  ```
 *
 * The version of the OpenAPI document: 0.0.42
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
import java.util.Arrays;
import java.util.UUID;

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
 * Product
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Product {
  public static final String SERIALIZED_NAME_AVERAGE_COST_PRICE = "average_cost_price";
  @SerializedName(SERIALIZED_NAME_AVERAGE_COST_PRICE)
  private Double averageCostPrice;

  public static final String SERIALIZED_NAME_BARCODE = "barcode";
  @SerializedName(SERIALIZED_NAME_BARCODE)
  private String barcode;

  public static final String SERIALIZED_NAME_BUYING_PRICE = "buying_price";
  @SerializedName(SERIALIZED_NAME_BUYING_PRICE)
  private Double buyingPrice;

  public static final String SERIALIZED_NAME_CENTIGA_ID = "centiga_id";
  @SerializedName(SERIALIZED_NAME_CENTIGA_ID)
  private String centigaId;

  public static final String SERIALIZED_NAME_COMPANY_ID = "company_id";
  @SerializedName(SERIALIZED_NAME_COMPANY_ID)
  private UUID companyId;

  public static final String SERIALIZED_NAME_CREATED = "created";
  @SerializedName(SERIALIZED_NAME_CREATED)
  private String created;

  public static final String SERIALIZED_NAME_CREATED_BY_ID = "created_by_id";
  @SerializedName(SERIALIZED_NAME_CREATED_BY_ID)
  private UUID createdById;

  public static final String SERIALIZED_NAME_DELETED = "deleted";
  @SerializedName(SERIALIZED_NAME_DELETED)
  private String deleted;

  public static final String SERIALIZED_NAME_DESCRIPTION = "description";
  @SerializedName(SERIALIZED_NAME_DESCRIPTION)
  private String description;

  public static final String SERIALIZED_NAME_ERP_ID = "erp_id";
  @SerializedName(SERIALIZED_NAME_ERP_ID)
  private String erpId;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_MODIFIED = "modified";
  @SerializedName(SERIALIZED_NAME_MODIFIED)
  private String modified;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_POGO_ID = "pogo_id";
  @SerializedName(SERIALIZED_NAME_POGO_ID)
  private String pogoId;

  public static final String SERIALIZED_NAME_PRODUCT_NUMBER = "product_number";
  @SerializedName(SERIALIZED_NAME_PRODUCT_NUMBER)
  private String productNumber;

  public static final String SERIALIZED_NAME_PROJECT_STATUS_TYPE_ID = "project_status_type_id";
  @SerializedName(SERIALIZED_NAME_PROJECT_STATUS_TYPE_ID)
  private UUID projectStatusTypeId;

  public static final String SERIALIZED_NAME_SELLING_PRICE = "selling_price";
  @SerializedName(SERIALIZED_NAME_SELLING_PRICE)
  private Double sellingPrice;

  public static final String SERIALIZED_NAME_TRIPLETEX_ID = "tripletex_id";
  @SerializedName(SERIALIZED_NAME_TRIPLETEX_ID)
  private String tripletexId;

  public Product() {
  }

  public Product(
     String created, 
     String deleted, 
     String modified
  ) {
    this();
    this.created = created;
    this.deleted = deleted;
    this.modified = modified;
  }

  public Product averageCostPrice(Double averageCostPrice) {
    this.averageCostPrice = averageCostPrice;
    return this;
  }

  /**
   * Get averageCostPrice
   * @return averageCostPrice
   */
  @javax.annotation.Nullable
  public Double getAverageCostPrice() {
    return averageCostPrice;
  }

  public void setAverageCostPrice(Double averageCostPrice) {
    this.averageCostPrice = averageCostPrice;
  }


  public Product barcode(String barcode) {
    this.barcode = barcode;
    return this;
  }

  /**
   * Get barcode
   * @return barcode
   */
  @javax.annotation.Nullable
  public String getBarcode() {
    return barcode;
  }

  public void setBarcode(String barcode) {
    this.barcode = barcode;
  }


  public Product buyingPrice(Double buyingPrice) {
    this.buyingPrice = buyingPrice;
    return this;
  }

  /**
   * Get buyingPrice
   * @return buyingPrice
   */
  @javax.annotation.Nullable
  public Double getBuyingPrice() {
    return buyingPrice;
  }

  public void setBuyingPrice(Double buyingPrice) {
    this.buyingPrice = buyingPrice;
  }


  public Product centigaId(String centigaId) {
    this.centigaId = centigaId;
    return this;
  }

  /**
   * Get centigaId
   * @return centigaId
   */
  @javax.annotation.Nullable
  public String getCentigaId() {
    return centigaId;
  }

  public void setCentigaId(String centigaId) {
    this.centigaId = centigaId;
  }


  public Product companyId(UUID companyId) {
    this.companyId = companyId;
    return this;
  }

  /**
   * Get companyId
   * @return companyId
   */
  @javax.annotation.Nullable
  public UUID getCompanyId() {
    return companyId;
  }

  public void setCompanyId(UUID companyId) {
    this.companyId = companyId;
  }


  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public String getCreated() {
    return created;
  }



  public Product createdById(UUID createdById) {
    this.createdById = createdById;
    return this;
  }

  /**
   * Get createdById
   * @return createdById
   */
  @javax.annotation.Nullable
  public UUID getCreatedById() {
    return createdById;
  }

  public void setCreatedById(UUID createdById) {
    this.createdById = createdById;
  }


  /**
   * Only present if it&#39;s a deleted object
   * @return deleted
   */
  @javax.annotation.Nullable
  public String getDeleted() {
    return deleted;
  }



  public Product description(String description) {
    this.description = description;
    return this;
  }

  /**
   * Get description
   * @return description
   */
  @javax.annotation.Nullable
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  public Product erpId(String erpId) {
    this.erpId = erpId;
    return this;
  }

  /**
   * Get erpId
   * @return erpId
   */
  @javax.annotation.Nullable
  public String getErpId() {
    return erpId;
  }

  public void setErpId(String erpId) {
    this.erpId = erpId;
  }


  public Product id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  /**
   * Get modified
   * @return modified
   */
  @javax.annotation.Nullable
  public String getModified() {
    return modified;
  }



  public Product name(String name) {
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


  public Product pogoId(String pogoId) {
    this.pogoId = pogoId;
    return this;
  }

  /**
   * Get pogoId
   * @return pogoId
   */
  @javax.annotation.Nullable
  public String getPogoId() {
    return pogoId;
  }

  public void setPogoId(String pogoId) {
    this.pogoId = pogoId;
  }


  public Product productNumber(String productNumber) {
    this.productNumber = productNumber;
    return this;
  }

  /**
   * Get productNumber
   * @return productNumber
   */
  @javax.annotation.Nullable
  public String getProductNumber() {
    return productNumber;
  }

  public void setProductNumber(String productNumber) {
    this.productNumber = productNumber;
  }


  public Product projectStatusTypeId(UUID projectStatusTypeId) {
    this.projectStatusTypeId = projectStatusTypeId;
    return this;
  }

  /**
   * Get projectStatusTypeId
   * @return projectStatusTypeId
   */
  @javax.annotation.Nullable
  public UUID getProjectStatusTypeId() {
    return projectStatusTypeId;
  }

  public void setProjectStatusTypeId(UUID projectStatusTypeId) {
    this.projectStatusTypeId = projectStatusTypeId;
  }


  public Product sellingPrice(Double sellingPrice) {
    this.sellingPrice = sellingPrice;
    return this;
  }

  /**
   * Get sellingPrice
   * @return sellingPrice
   */
  @javax.annotation.Nullable
  public Double getSellingPrice() {
    return sellingPrice;
  }

  public void setSellingPrice(Double sellingPrice) {
    this.sellingPrice = sellingPrice;
  }


  public Product tripletexId(String tripletexId) {
    this.tripletexId = tripletexId;
    return this;
  }

  /**
   * Get tripletexId
   * @return tripletexId
   */
  @javax.annotation.Nullable
  public String getTripletexId() {
    return tripletexId;
  }

  public void setTripletexId(String tripletexId) {
    this.tripletexId = tripletexId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Product product = (Product) o;
    return Objects.equals(this.averageCostPrice, product.averageCostPrice) &&
        Objects.equals(this.barcode, product.barcode) &&
        Objects.equals(this.buyingPrice, product.buyingPrice) &&
        Objects.equals(this.centigaId, product.centigaId) &&
        Objects.equals(this.companyId, product.companyId) &&
        Objects.equals(this.created, product.created) &&
        Objects.equals(this.createdById, product.createdById) &&
        Objects.equals(this.deleted, product.deleted) &&
        Objects.equals(this.description, product.description) &&
        Objects.equals(this.erpId, product.erpId) &&
        Objects.equals(this.id, product.id) &&
        Objects.equals(this.modified, product.modified) &&
        Objects.equals(this.name, product.name) &&
        Objects.equals(this.pogoId, product.pogoId) &&
        Objects.equals(this.productNumber, product.productNumber) &&
        Objects.equals(this.projectStatusTypeId, product.projectStatusTypeId) &&
        Objects.equals(this.sellingPrice, product.sellingPrice) &&
        Objects.equals(this.tripletexId, product.tripletexId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(averageCostPrice, barcode, buyingPrice, centigaId, companyId, created, createdById, deleted, description, erpId, id, modified, name, pogoId, productNumber, projectStatusTypeId, sellingPrice, tripletexId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Product {\n");
    sb.append("    averageCostPrice: ").append(toIndentedString(averageCostPrice)).append("\n");
    sb.append("    barcode: ").append(toIndentedString(barcode)).append("\n");
    sb.append("    buyingPrice: ").append(toIndentedString(buyingPrice)).append("\n");
    sb.append("    centigaId: ").append(toIndentedString(centigaId)).append("\n");
    sb.append("    companyId: ").append(toIndentedString(companyId)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    createdById: ").append(toIndentedString(createdById)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    erpId: ").append(toIndentedString(erpId)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    modified: ").append(toIndentedString(modified)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    pogoId: ").append(toIndentedString(pogoId)).append("\n");
    sb.append("    productNumber: ").append(toIndentedString(productNumber)).append("\n");
    sb.append("    projectStatusTypeId: ").append(toIndentedString(projectStatusTypeId)).append("\n");
    sb.append("    sellingPrice: ").append(toIndentedString(sellingPrice)).append("\n");
    sb.append("    tripletexId: ").append(toIndentedString(tripletexId)).append("\n");
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
    openapiFields.add("average_cost_price");
    openapiFields.add("barcode");
    openapiFields.add("buying_price");
    openapiFields.add("centiga_id");
    openapiFields.add("company_id");
    openapiFields.add("created");
    openapiFields.add("created_by_id");
    openapiFields.add("deleted");
    openapiFields.add("description");
    openapiFields.add("erp_id");
    openapiFields.add("id");
    openapiFields.add("modified");
    openapiFields.add("name");
    openapiFields.add("pogo_id");
    openapiFields.add("product_number");
    openapiFields.add("project_status_type_id");
    openapiFields.add("selling_price");
    openapiFields.add("tripletex_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Product
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Product.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Product is not found in the empty JSON string", Product.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Product.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Product` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("barcode") != null && !jsonObj.get("barcode").isJsonNull()) && !jsonObj.get("barcode").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `barcode` to be a primitive type in the JSON string but got `%s`", jsonObj.get("barcode").toString()));
      }
      if ((jsonObj.get("centiga_id") != null && !jsonObj.get("centiga_id").isJsonNull()) && !jsonObj.get("centiga_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `centiga_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("centiga_id").toString()));
      }
      if ((jsonObj.get("company_id") != null && !jsonObj.get("company_id").isJsonNull()) && !jsonObj.get("company_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_id").toString()));
      }
      if ((jsonObj.get("created") != null && !jsonObj.get("created").isJsonNull()) && !jsonObj.get("created").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created").toString()));
      }
      if ((jsonObj.get("created_by_id") != null && !jsonObj.get("created_by_id").isJsonNull()) && !jsonObj.get("created_by_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `created_by_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("created_by_id").toString()));
      }
      if ((jsonObj.get("deleted") != null && !jsonObj.get("deleted").isJsonNull()) && !jsonObj.get("deleted").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `deleted` to be a primitive type in the JSON string but got `%s`", jsonObj.get("deleted").toString()));
      }
      if ((jsonObj.get("description") != null && !jsonObj.get("description").isJsonNull()) && !jsonObj.get("description").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `description` to be a primitive type in the JSON string but got `%s`", jsonObj.get("description").toString()));
      }
      if ((jsonObj.get("erp_id") != null && !jsonObj.get("erp_id").isJsonNull()) && !jsonObj.get("erp_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `erp_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("erp_id").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("modified") != null && !jsonObj.get("modified").isJsonNull()) && !jsonObj.get("modified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("pogo_id") != null && !jsonObj.get("pogo_id").isJsonNull()) && !jsonObj.get("pogo_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pogo_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pogo_id").toString()));
      }
      if ((jsonObj.get("product_number") != null && !jsonObj.get("product_number").isJsonNull()) && !jsonObj.get("product_number").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `product_number` to be a primitive type in the JSON string but got `%s`", jsonObj.get("product_number").toString()));
      }
      if ((jsonObj.get("project_status_type_id") != null && !jsonObj.get("project_status_type_id").isJsonNull()) && !jsonObj.get("project_status_type_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `project_status_type_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("project_status_type_id").toString()));
      }
      if ((jsonObj.get("tripletex_id") != null && !jsonObj.get("tripletex_id").isJsonNull()) && !jsonObj.get("tripletex_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tripletex_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tripletex_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Product.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Product' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Product> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Product.class));

       return (TypeAdapter<T>) new TypeAdapter<Product>() {
           @Override
           public void write(JsonWriter out, Product value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Product read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Product given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Product
   * @throws IOException if the JSON string is invalid with respect to Product
   */
  public static Product fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Product.class);
  }

  /**
   * Convert an instance of Product to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

