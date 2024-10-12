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
import java.math.BigDecimal;
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
 * Project
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Project {
  public static final String SERIALIZED_NAME_CITY_ID = "city_id";
  @SerializedName(SERIALIZED_NAME_CITY_ID)
  private UUID cityId;

  public static final String SERIALIZED_NAME_COMPANY_ID = "company_id";
  @SerializedName(SERIALIZED_NAME_COMPANY_ID)
  private UUID companyId;

  public static final String SERIALIZED_NAME_CONTACT_ID = "contact_id";
  @SerializedName(SERIALIZED_NAME_CONTACT_ID)
  private UUID contactId;

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

  public static final String SERIALIZED_NAME_END_TIME = "end_time";
  @SerializedName(SERIALIZED_NAME_END_TIME)
  private String endTime;

  public static final String SERIALIZED_NAME_ERP_PROJECT_ID = "erp_project_id";
  @SerializedName(SERIALIZED_NAME_ERP_PROJECT_ID)
  private String erpProjectId;

  public static final String SERIALIZED_NAME_ERP_TASK_ID = "erp_task_id";
  @SerializedName(SERIALIZED_NAME_ERP_TASK_ID)
  private String erpTaskId;

  public static final String SERIALIZED_NAME_FULL_NAME = "full_name";
  @SerializedName(SERIALIZED_NAME_FULL_NAME)
  private String fullName;

  public static final String SERIALIZED_NAME_HAS_FINAL_INVOICE = "has_final_invoice";
  @SerializedName(SERIALIZED_NAME_HAS_FINAL_INVOICE)
  private Boolean hasFinalInvoice;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_IS_FIXED_PRICE = "is_fixed_price";
  @SerializedName(SERIALIZED_NAME_IS_FIXED_PRICE)
  private Boolean isFixedPrice;

  public static final String SERIALIZED_NAME_IS_OFFER = "is_offer";
  @SerializedName(SERIALIZED_NAME_IS_OFFER)
  private Boolean isOffer;

  public static final String SERIALIZED_NAME_IS_ROTTEN = "is_rotten";
  @SerializedName(SERIALIZED_NAME_IS_ROTTEN)
  private String isRotten;

  public static final String SERIALIZED_NAME_LATITUDE = "latitude";
  @SerializedName(SERIALIZED_NAME_LATITUDE)
  private String latitude;

  public static final String SERIALIZED_NAME_LONGITUDE = "longitude";
  @SerializedName(SERIALIZED_NAME_LONGITUDE)
  private String longitude;

  public static final String SERIALIZED_NAME_MODIFIED = "modified";
  @SerializedName(SERIALIZED_NAME_MODIFIED)
  private String modified;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_NOT_INVOICED_AMOUNT = "not_invoiced_amount";
  @SerializedName(SERIALIZED_NAME_NOT_INVOICED_AMOUNT)
  private Float notInvoicedAmount;

  public static final String SERIALIZED_NAME_OFFER_ID = "offer_id";
  @SerializedName(SERIALIZED_NAME_OFFER_ID)
  private UUID offerId;

  public static final String SERIALIZED_NAME_PARENT_ID = "parent_id";
  @SerializedName(SERIALIZED_NAME_PARENT_ID)
  private UUID parentId;

  public static final String SERIALIZED_NAME_PRE_CALCULATION_ID = "pre_calculation_id";
  @SerializedName(SERIALIZED_NAME_PRE_CALCULATION_ID)
  private UUID preCalculationId;

  public static final String SERIALIZED_NAME_PRODUCTS_TOTAL_COST_PRICE = "products_total_cost_price";
  @SerializedName(SERIALIZED_NAME_PRODUCTS_TOTAL_COST_PRICE)
  private Float productsTotalCostPrice;

  public static final String SERIALIZED_NAME_PROJECT_IMAGE_URL = "project_image_url";
  @SerializedName(SERIALIZED_NAME_PROJECT_IMAGE_URL)
  private String projectImageUrl;

  public static final String SERIALIZED_NAME_PROJECT_NUMBER = "project_number";
  @SerializedName(SERIALIZED_NAME_PROJECT_NUMBER)
  private BigDecimal projectNumber;

  public static final String SERIALIZED_NAME_PROJECT_STATUS_ID = "project_status_id";
  @SerializedName(SERIALIZED_NAME_PROJECT_STATUS_ID)
  private UUID projectStatusId;

  public static final String SERIALIZED_NAME_SHARED_PROJECT_ID = "shared_project_id";
  @SerializedName(SERIALIZED_NAME_SHARED_PROJECT_ID)
  private UUID sharedProjectId;

  public static final String SERIALIZED_NAME_START_TIME = "start_time";
  @SerializedName(SERIALIZED_NAME_START_TIME)
  private String startTime;

  public static final String SERIALIZED_NAME_STREET_NAME = "street_name";
  @SerializedName(SERIALIZED_NAME_STREET_NAME)
  private String streetName;

  public static final String SERIALIZED_NAME_THUMBNAIL = "thumbnail";
  @SerializedName(SERIALIZED_NAME_THUMBNAIL)
  private String thumbnail;

  public static final String SERIALIZED_NAME_TOTAL_SALES_PRICE = "total_sales_price";
  @SerializedName(SERIALIZED_NAME_TOTAL_SALES_PRICE)
  private Float totalSalesPrice;

  public static final String SERIALIZED_NAME_WORKING_HOURS_TOTAL_COST_PRICE = "working_hours_total_cost_price";
  @SerializedName(SERIALIZED_NAME_WORKING_HOURS_TOTAL_COST_PRICE)
  private Float workingHoursTotalCostPrice;

  public Project() {
  }

  public Project(
     String created, 
     String deleted, 
     String modified
  ) {
    this();
    this.created = created;
    this.deleted = deleted;
    this.modified = modified;
  }

  public Project cityId(UUID cityId) {
    this.cityId = cityId;
    return this;
  }

  /**
   * Get cityId
   * @return cityId
   */
  @javax.annotation.Nullable
  public UUID getCityId() {
    return cityId;
  }

  public void setCityId(UUID cityId) {
    this.cityId = cityId;
  }


  public Project companyId(UUID companyId) {
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


  public Project contactId(UUID contactId) {
    this.contactId = contactId;
    return this;
  }

  /**
   * Get contactId
   * @return contactId
   */
  @javax.annotation.Nullable
  public UUID getContactId() {
    return contactId;
  }

  public void setContactId(UUID contactId) {
    this.contactId = contactId;
  }


  /**
   * Get created
   * @return created
   */
  @javax.annotation.Nullable
  public String getCreated() {
    return created;
  }



  public Project createdById(UUID createdById) {
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



  public Project description(String description) {
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


  public Project endTime(String endTime) {
    this.endTime = endTime;
    return this;
  }

  /**
   * Get endTime
   * @return endTime
   */
  @javax.annotation.Nullable
  public String getEndTime() {
    return endTime;
  }

  public void setEndTime(String endTime) {
    this.endTime = endTime;
  }


  public Project erpProjectId(String erpProjectId) {
    this.erpProjectId = erpProjectId;
    return this;
  }

  /**
   * Get erpProjectId
   * @return erpProjectId
   */
  @javax.annotation.Nullable
  public String getErpProjectId() {
    return erpProjectId;
  }

  public void setErpProjectId(String erpProjectId) {
    this.erpProjectId = erpProjectId;
  }


  public Project erpTaskId(String erpTaskId) {
    this.erpTaskId = erpTaskId;
    return this;
  }

  /**
   * Get erpTaskId
   * @return erpTaskId
   */
  @javax.annotation.Nullable
  public String getErpTaskId() {
    return erpTaskId;
  }

  public void setErpTaskId(String erpTaskId) {
    this.erpTaskId = erpTaskId;
  }


  public Project fullName(String fullName) {
    this.fullName = fullName;
    return this;
  }

  /**
   * Project number + name
   * @return fullName
   */
  @javax.annotation.Nullable
  public String getFullName() {
    return fullName;
  }

  public void setFullName(String fullName) {
    this.fullName = fullName;
  }


  public Project hasFinalInvoice(Boolean hasFinalInvoice) {
    this.hasFinalInvoice = hasFinalInvoice;
    return this;
  }

  /**
   * Is there at least one final invoice
   * @return hasFinalInvoice
   */
  @javax.annotation.Nullable
  public Boolean getHasFinalInvoice() {
    return hasFinalInvoice;
  }

  public void setHasFinalInvoice(Boolean hasFinalInvoice) {
    this.hasFinalInvoice = hasFinalInvoice;
  }


  public Project id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Get id
   * @return id
   */
  @javax.annotation.Nonnull
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public Project isFixedPrice(Boolean isFixedPrice) {
    this.isFixedPrice = isFixedPrice;
    return this;
  }

  /**
   * Get isFixedPrice
   * @return isFixedPrice
   */
  @javax.annotation.Nullable
  public Boolean getIsFixedPrice() {
    return isFixedPrice;
  }

  public void setIsFixedPrice(Boolean isFixedPrice) {
    this.isFixedPrice = isFixedPrice;
  }


  public Project isOffer(Boolean isOffer) {
    this.isOffer = isOffer;
    return this;
  }

  /**
   * Is the project was offer
   * @return isOffer
   */
  @javax.annotation.Nullable
  public Boolean getIsOffer() {
    return isOffer;
  }

  public void setIsOffer(Boolean isOffer) {
    this.isOffer = isOffer;
  }


  public Project isRotten(String isRotten) {
    this.isRotten = isRotten;
    return this;
  }

  /**
   * Last form date - read-only
   * @return isRotten
   */
  @javax.annotation.Nullable
  public String getIsRotten() {
    return isRotten;
  }

  public void setIsRotten(String isRotten) {
    this.isRotten = isRotten;
  }


  public Project latitude(String latitude) {
    this.latitude = latitude;
    return this;
  }

  /**
   * Get latitude
   * @return latitude
   */
  @javax.annotation.Nullable
  public String getLatitude() {
    return latitude;
  }

  public void setLatitude(String latitude) {
    this.latitude = latitude;
  }


  public Project longitude(String longitude) {
    this.longitude = longitude;
    return this;
  }

  /**
   * Get longitude
   * @return longitude
   */
  @javax.annotation.Nullable
  public String getLongitude() {
    return longitude;
  }

  public void setLongitude(String longitude) {
    this.longitude = longitude;
  }


  /**
   * Get modified
   * @return modified
   */
  @javax.annotation.Nullable
  public String getModified() {
    return modified;
  }



  public Project name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Get name
   * @return name
   */
  @javax.annotation.Nonnull
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Project notInvoicedAmount(Float notInvoicedAmount) {
    this.notInvoicedAmount = notInvoicedAmount;
    return this;
  }

  /**
   * Get notInvoicedAmount
   * @return notInvoicedAmount
   */
  @javax.annotation.Nullable
  public Float getNotInvoicedAmount() {
    return notInvoicedAmount;
  }

  public void setNotInvoicedAmount(Float notInvoicedAmount) {
    this.notInvoicedAmount = notInvoicedAmount;
  }


  public Project offerId(UUID offerId) {
    this.offerId = offerId;
    return this;
  }

  /**
   * Get offerId
   * @return offerId
   */
  @javax.annotation.Nullable
  public UUID getOfferId() {
    return offerId;
  }

  public void setOfferId(UUID offerId) {
    this.offerId = offerId;
  }


  public Project parentId(UUID parentId) {
    this.parentId = parentId;
    return this;
  }

  /**
   * Get parentId
   * @return parentId
   */
  @javax.annotation.Nullable
  public UUID getParentId() {
    return parentId;
  }

  public void setParentId(UUID parentId) {
    this.parentId = parentId;
  }


  public Project preCalculationId(UUID preCalculationId) {
    this.preCalculationId = preCalculationId;
    return this;
  }

  /**
   * Get preCalculationId
   * @return preCalculationId
   */
  @javax.annotation.Nullable
  public UUID getPreCalculationId() {
    return preCalculationId;
  }

  public void setPreCalculationId(UUID preCalculationId) {
    this.preCalculationId = preCalculationId;
  }


  public Project productsTotalCostPrice(Float productsTotalCostPrice) {
    this.productsTotalCostPrice = productsTotalCostPrice;
    return this;
  }

  /**
   * Get productsTotalCostPrice
   * @return productsTotalCostPrice
   */
  @javax.annotation.Nullable
  public Float getProductsTotalCostPrice() {
    return productsTotalCostPrice;
  }

  public void setProductsTotalCostPrice(Float productsTotalCostPrice) {
    this.productsTotalCostPrice = productsTotalCostPrice;
  }


  public Project projectImageUrl(String projectImageUrl) {
    this.projectImageUrl = projectImageUrl;
    return this;
  }

  /**
   * Get projectImageUrl
   * @return projectImageUrl
   */
  @javax.annotation.Nullable
  public String getProjectImageUrl() {
    return projectImageUrl;
  }

  public void setProjectImageUrl(String projectImageUrl) {
    this.projectImageUrl = projectImageUrl;
  }


  public Project projectNumber(BigDecimal projectNumber) {
    this.projectNumber = projectNumber;
    return this;
  }

  /**
   * Get projectNumber
   * @return projectNumber
   */
  @javax.annotation.Nullable
  public BigDecimal getProjectNumber() {
    return projectNumber;
  }

  public void setProjectNumber(BigDecimal projectNumber) {
    this.projectNumber = projectNumber;
  }


  public Project projectStatusId(UUID projectStatusId) {
    this.projectStatusId = projectStatusId;
    return this;
  }

  /**
   * Get projectStatusId
   * @return projectStatusId
   */
  @javax.annotation.Nullable
  public UUID getProjectStatusId() {
    return projectStatusId;
  }

  public void setProjectStatusId(UUID projectStatusId) {
    this.projectStatusId = projectStatusId;
  }


  public Project sharedProjectId(UUID sharedProjectId) {
    this.sharedProjectId = sharedProjectId;
    return this;
  }

  /**
   * Get sharedProjectId
   * @return sharedProjectId
   */
  @javax.annotation.Nullable
  public UUID getSharedProjectId() {
    return sharedProjectId;
  }

  public void setSharedProjectId(UUID sharedProjectId) {
    this.sharedProjectId = sharedProjectId;
  }


  public Project startTime(String startTime) {
    this.startTime = startTime;
    return this;
  }

  /**
   * Get startTime
   * @return startTime
   */
  @javax.annotation.Nullable
  public String getStartTime() {
    return startTime;
  }

  public void setStartTime(String startTime) {
    this.startTime = startTime;
  }


  public Project streetName(String streetName) {
    this.streetName = streetName;
    return this;
  }

  /**
   * Get streetName
   * @return streetName
   */
  @javax.annotation.Nullable
  public String getStreetName() {
    return streetName;
  }

  public void setStreetName(String streetName) {
    this.streetName = streetName;
  }


  public Project thumbnail(String thumbnail) {
    this.thumbnail = thumbnail;
    return this;
  }

  /**
   * Get thumbnail
   * @return thumbnail
   */
  @javax.annotation.Nullable
  public String getThumbnail() {
    return thumbnail;
  }

  public void setThumbnail(String thumbnail) {
    this.thumbnail = thumbnail;
  }


  public Project totalSalesPrice(Float totalSalesPrice) {
    this.totalSalesPrice = totalSalesPrice;
    return this;
  }

  /**
   * Get totalSalesPrice
   * @return totalSalesPrice
   */
  @javax.annotation.Nullable
  public Float getTotalSalesPrice() {
    return totalSalesPrice;
  }

  public void setTotalSalesPrice(Float totalSalesPrice) {
    this.totalSalesPrice = totalSalesPrice;
  }


  public Project workingHoursTotalCostPrice(Float workingHoursTotalCostPrice) {
    this.workingHoursTotalCostPrice = workingHoursTotalCostPrice;
    return this;
  }

  /**
   * Get workingHoursTotalCostPrice
   * @return workingHoursTotalCostPrice
   */
  @javax.annotation.Nullable
  public Float getWorkingHoursTotalCostPrice() {
    return workingHoursTotalCostPrice;
  }

  public void setWorkingHoursTotalCostPrice(Float workingHoursTotalCostPrice) {
    this.workingHoursTotalCostPrice = workingHoursTotalCostPrice;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Project project = (Project) o;
    return Objects.equals(this.cityId, project.cityId) &&
        Objects.equals(this.companyId, project.companyId) &&
        Objects.equals(this.contactId, project.contactId) &&
        Objects.equals(this.created, project.created) &&
        Objects.equals(this.createdById, project.createdById) &&
        Objects.equals(this.deleted, project.deleted) &&
        Objects.equals(this.description, project.description) &&
        Objects.equals(this.endTime, project.endTime) &&
        Objects.equals(this.erpProjectId, project.erpProjectId) &&
        Objects.equals(this.erpTaskId, project.erpTaskId) &&
        Objects.equals(this.fullName, project.fullName) &&
        Objects.equals(this.hasFinalInvoice, project.hasFinalInvoice) &&
        Objects.equals(this.id, project.id) &&
        Objects.equals(this.isFixedPrice, project.isFixedPrice) &&
        Objects.equals(this.isOffer, project.isOffer) &&
        Objects.equals(this.isRotten, project.isRotten) &&
        Objects.equals(this.latitude, project.latitude) &&
        Objects.equals(this.longitude, project.longitude) &&
        Objects.equals(this.modified, project.modified) &&
        Objects.equals(this.name, project.name) &&
        Objects.equals(this.notInvoicedAmount, project.notInvoicedAmount) &&
        Objects.equals(this.offerId, project.offerId) &&
        Objects.equals(this.parentId, project.parentId) &&
        Objects.equals(this.preCalculationId, project.preCalculationId) &&
        Objects.equals(this.productsTotalCostPrice, project.productsTotalCostPrice) &&
        Objects.equals(this.projectImageUrl, project.projectImageUrl) &&
        Objects.equals(this.projectNumber, project.projectNumber) &&
        Objects.equals(this.projectStatusId, project.projectStatusId) &&
        Objects.equals(this.sharedProjectId, project.sharedProjectId) &&
        Objects.equals(this.startTime, project.startTime) &&
        Objects.equals(this.streetName, project.streetName) &&
        Objects.equals(this.thumbnail, project.thumbnail) &&
        Objects.equals(this.totalSalesPrice, project.totalSalesPrice) &&
        Objects.equals(this.workingHoursTotalCostPrice, project.workingHoursTotalCostPrice);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cityId, companyId, contactId, created, createdById, deleted, description, endTime, erpProjectId, erpTaskId, fullName, hasFinalInvoice, id, isFixedPrice, isOffer, isRotten, latitude, longitude, modified, name, notInvoicedAmount, offerId, parentId, preCalculationId, productsTotalCostPrice, projectImageUrl, projectNumber, projectStatusId, sharedProjectId, startTime, streetName, thumbnail, totalSalesPrice, workingHoursTotalCostPrice);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Project {\n");
    sb.append("    cityId: ").append(toIndentedString(cityId)).append("\n");
    sb.append("    companyId: ").append(toIndentedString(companyId)).append("\n");
    sb.append("    contactId: ").append(toIndentedString(contactId)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    createdById: ").append(toIndentedString(createdById)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    endTime: ").append(toIndentedString(endTime)).append("\n");
    sb.append("    erpProjectId: ").append(toIndentedString(erpProjectId)).append("\n");
    sb.append("    erpTaskId: ").append(toIndentedString(erpTaskId)).append("\n");
    sb.append("    fullName: ").append(toIndentedString(fullName)).append("\n");
    sb.append("    hasFinalInvoice: ").append(toIndentedString(hasFinalInvoice)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isFixedPrice: ").append(toIndentedString(isFixedPrice)).append("\n");
    sb.append("    isOffer: ").append(toIndentedString(isOffer)).append("\n");
    sb.append("    isRotten: ").append(toIndentedString(isRotten)).append("\n");
    sb.append("    latitude: ").append(toIndentedString(latitude)).append("\n");
    sb.append("    longitude: ").append(toIndentedString(longitude)).append("\n");
    sb.append("    modified: ").append(toIndentedString(modified)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    notInvoicedAmount: ").append(toIndentedString(notInvoicedAmount)).append("\n");
    sb.append("    offerId: ").append(toIndentedString(offerId)).append("\n");
    sb.append("    parentId: ").append(toIndentedString(parentId)).append("\n");
    sb.append("    preCalculationId: ").append(toIndentedString(preCalculationId)).append("\n");
    sb.append("    productsTotalCostPrice: ").append(toIndentedString(productsTotalCostPrice)).append("\n");
    sb.append("    projectImageUrl: ").append(toIndentedString(projectImageUrl)).append("\n");
    sb.append("    projectNumber: ").append(toIndentedString(projectNumber)).append("\n");
    sb.append("    projectStatusId: ").append(toIndentedString(projectStatusId)).append("\n");
    sb.append("    sharedProjectId: ").append(toIndentedString(sharedProjectId)).append("\n");
    sb.append("    startTime: ").append(toIndentedString(startTime)).append("\n");
    sb.append("    streetName: ").append(toIndentedString(streetName)).append("\n");
    sb.append("    thumbnail: ").append(toIndentedString(thumbnail)).append("\n");
    sb.append("    totalSalesPrice: ").append(toIndentedString(totalSalesPrice)).append("\n");
    sb.append("    workingHoursTotalCostPrice: ").append(toIndentedString(workingHoursTotalCostPrice)).append("\n");
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
    openapiFields.add("city_id");
    openapiFields.add("company_id");
    openapiFields.add("contact_id");
    openapiFields.add("created");
    openapiFields.add("created_by_id");
    openapiFields.add("deleted");
    openapiFields.add("description");
    openapiFields.add("end_time");
    openapiFields.add("erp_project_id");
    openapiFields.add("erp_task_id");
    openapiFields.add("full_name");
    openapiFields.add("has_final_invoice");
    openapiFields.add("id");
    openapiFields.add("is_fixed_price");
    openapiFields.add("is_offer");
    openapiFields.add("is_rotten");
    openapiFields.add("latitude");
    openapiFields.add("longitude");
    openapiFields.add("modified");
    openapiFields.add("name");
    openapiFields.add("not_invoiced_amount");
    openapiFields.add("offer_id");
    openapiFields.add("parent_id");
    openapiFields.add("pre_calculation_id");
    openapiFields.add("products_total_cost_price");
    openapiFields.add("project_image_url");
    openapiFields.add("project_number");
    openapiFields.add("project_status_id");
    openapiFields.add("shared_project_id");
    openapiFields.add("start_time");
    openapiFields.add("street_name");
    openapiFields.add("thumbnail");
    openapiFields.add("total_sales_price");
    openapiFields.add("working_hours_total_cost_price");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
    openapiRequiredFields.add("name");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Project
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Project.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Project is not found in the empty JSON string", Project.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Project.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Project` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Project.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("city_id") != null && !jsonObj.get("city_id").isJsonNull()) && !jsonObj.get("city_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `city_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("city_id").toString()));
      }
      if ((jsonObj.get("company_id") != null && !jsonObj.get("company_id").isJsonNull()) && !jsonObj.get("company_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `company_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("company_id").toString()));
      }
      if ((jsonObj.get("contact_id") != null && !jsonObj.get("contact_id").isJsonNull()) && !jsonObj.get("contact_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `contact_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("contact_id").toString()));
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
      if ((jsonObj.get("end_time") != null && !jsonObj.get("end_time").isJsonNull()) && !jsonObj.get("end_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `end_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("end_time").toString()));
      }
      if ((jsonObj.get("erp_project_id") != null && !jsonObj.get("erp_project_id").isJsonNull()) && !jsonObj.get("erp_project_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `erp_project_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("erp_project_id").toString()));
      }
      if ((jsonObj.get("erp_task_id") != null && !jsonObj.get("erp_task_id").isJsonNull()) && !jsonObj.get("erp_task_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `erp_task_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("erp_task_id").toString()));
      }
      if ((jsonObj.get("full_name") != null && !jsonObj.get("full_name").isJsonNull()) && !jsonObj.get("full_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `full_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("full_name").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("is_offer") != null && !jsonObj.get("is_offer").isJsonNull()) && !jsonObj.get("is_offer").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `is_offer` to be a primitive type in the JSON string but got `%s`", jsonObj.get("is_offer").toString()));
      }
      if ((jsonObj.get("is_rotten") != null && !jsonObj.get("is_rotten").isJsonNull()) && !jsonObj.get("is_rotten").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `is_rotten` to be a primitive type in the JSON string but got `%s`", jsonObj.get("is_rotten").toString()));
      }
      if ((jsonObj.get("latitude") != null && !jsonObj.get("latitude").isJsonNull()) && !jsonObj.get("latitude").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `latitude` to be a primitive type in the JSON string but got `%s`", jsonObj.get("latitude").toString()));
      }
      if ((jsonObj.get("longitude") != null && !jsonObj.get("longitude").isJsonNull()) && !jsonObj.get("longitude").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `longitude` to be a primitive type in the JSON string but got `%s`", jsonObj.get("longitude").toString()));
      }
      if ((jsonObj.get("modified") != null && !jsonObj.get("modified").isJsonNull()) && !jsonObj.get("modified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified").toString()));
      }
      if (!jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      if ((jsonObj.get("offer_id") != null && !jsonObj.get("offer_id").isJsonNull()) && !jsonObj.get("offer_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `offer_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("offer_id").toString()));
      }
      if ((jsonObj.get("parent_id") != null && !jsonObj.get("parent_id").isJsonNull()) && !jsonObj.get("parent_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `parent_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("parent_id").toString()));
      }
      if ((jsonObj.get("pre_calculation_id") != null && !jsonObj.get("pre_calculation_id").isJsonNull()) && !jsonObj.get("pre_calculation_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `pre_calculation_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("pre_calculation_id").toString()));
      }
      if ((jsonObj.get("project_image_url") != null && !jsonObj.get("project_image_url").isJsonNull()) && !jsonObj.get("project_image_url").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `project_image_url` to be a primitive type in the JSON string but got `%s`", jsonObj.get("project_image_url").toString()));
      }
      if ((jsonObj.get("project_status_id") != null && !jsonObj.get("project_status_id").isJsonNull()) && !jsonObj.get("project_status_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `project_status_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("project_status_id").toString()));
      }
      if ((jsonObj.get("shared_project_id") != null && !jsonObj.get("shared_project_id").isJsonNull()) && !jsonObj.get("shared_project_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `shared_project_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("shared_project_id").toString()));
      }
      if ((jsonObj.get("start_time") != null && !jsonObj.get("start_time").isJsonNull()) && !jsonObj.get("start_time").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `start_time` to be a primitive type in the JSON string but got `%s`", jsonObj.get("start_time").toString()));
      }
      if ((jsonObj.get("street_name") != null && !jsonObj.get("street_name").isJsonNull()) && !jsonObj.get("street_name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `street_name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("street_name").toString()));
      }
      if ((jsonObj.get("thumbnail") != null && !jsonObj.get("thumbnail").isJsonNull()) && !jsonObj.get("thumbnail").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `thumbnail` to be a primitive type in the JSON string but got `%s`", jsonObj.get("thumbnail").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Project.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Project' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Project> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Project.class));

       return (TypeAdapter<T>) new TypeAdapter<Project>() {
           @Override
           public void write(JsonWriter out, Project value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Project read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Project given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Project
   * @throws IOException if the JSON string is invalid with respect to Project
   */
  public static Project fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Project.class);
  }

  /**
   * Convert an instance of Project to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

