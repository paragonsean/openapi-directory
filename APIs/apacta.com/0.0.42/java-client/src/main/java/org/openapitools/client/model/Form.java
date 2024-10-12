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
import java.time.LocalDate;
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
 * Form
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:16.415087-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Form {
  public static final String SERIALIZED_NAME_APPROVED_BY_ID = "approved_by_id";
  @SerializedName(SERIALIZED_NAME_APPROVED_BY_ID)
  private UUID approvedById;

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

  public static final String SERIALIZED_NAME_FORM_DATE = "form_date";
  @SerializedName(SERIALIZED_NAME_FORM_DATE)
  private LocalDate formDate;

  public static final String SERIALIZED_NAME_FORM_TEMPLATE_ID = "form_template_id";
  @SerializedName(SERIALIZED_NAME_FORM_TEMPLATE_ID)
  private UUID formTemplateId;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private UUID id;

  public static final String SERIALIZED_NAME_IS_DRAFT = "is_draft";
  @SerializedName(SERIALIZED_NAME_IS_DRAFT)
  private Boolean isDraft = false;

  public static final String SERIALIZED_NAME_IS_INVOICED = "is_invoiced";
  @SerializedName(SERIALIZED_NAME_IS_INVOICED)
  private String isInvoiced;

  public static final String SERIALIZED_NAME_IS_SHARED = "is_shared";
  @SerializedName(SERIALIZED_NAME_IS_SHARED)
  private Boolean isShared = false;

  public static final String SERIALIZED_NAME_MASS_FORM_ID = "mass_form_id";
  @SerializedName(SERIALIZED_NAME_MASS_FORM_ID)
  private UUID massFormId;

  public static final String SERIALIZED_NAME_MODIFIED = "modified";
  @SerializedName(SERIALIZED_NAME_MODIFIED)
  private String modified;

  public static final String SERIALIZED_NAME_PROJECT_ID = "project_id";
  @SerializedName(SERIALIZED_NAME_PROJECT_ID)
  private UUID projectId;

  public Form() {
  }

  public Form(
     String created, 
     String deleted, 
     String modified
  ) {
    this();
    this.created = created;
    this.deleted = deleted;
    this.modified = modified;
  }

  public Form approvedById(UUID approvedById) {
    this.approvedById = approvedById;
    return this;
  }

  /**
   * Get approvedById
   * @return approvedById
   */
  @javax.annotation.Nullable
  public UUID getApprovedById() {
    return approvedById;
  }

  public void setApprovedById(UUID approvedById) {
    this.approvedById = approvedById;
  }


  public Form companyId(UUID companyId) {
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



  public Form createdById(UUID createdById) {
    this.createdById = createdById;
    return this;
  }

  /**
   * Read-only
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



  public Form formDate(LocalDate formDate) {
    this.formDate = formDate;
    return this;
  }

  /**
   * Get formDate
   * @return formDate
   */
  @javax.annotation.Nullable
  public LocalDate getFormDate() {
    return formDate;
  }

  public void setFormDate(LocalDate formDate) {
    this.formDate = formDate;
  }


  public Form formTemplateId(UUID formTemplateId) {
    this.formTemplateId = formTemplateId;
    return this;
  }

  /**
   * Get formTemplateId
   * @return formTemplateId
   */
  @javax.annotation.Nullable
  public UUID getFormTemplateId() {
    return formTemplateId;
  }

  public void setFormTemplateId(UUID formTemplateId) {
    this.formTemplateId = formTemplateId;
  }


  public Form id(UUID id) {
    this.id = id;
    return this;
  }

  /**
   * Read-only
   * @return id
   */
  @javax.annotation.Nullable
  public UUID getId() {
    return id;
  }

  public void setId(UUID id) {
    this.id = id;
  }


  public Form isDraft(Boolean isDraft) {
    this.isDraft = isDraft;
    return this;
  }

  /**
   * Get isDraft
   * @return isDraft
   */
  @javax.annotation.Nullable
  public Boolean getIsDraft() {
    return isDraft;
  }

  public void setIsDraft(Boolean isDraft) {
    this.isDraft = isDraft;
  }


  public Form isInvoiced(String isInvoiced) {
    this.isInvoiced = isInvoiced;
    return this;
  }

  /**
   * Get isInvoiced
   * @return isInvoiced
   */
  @javax.annotation.Nullable
  public String getIsInvoiced() {
    return isInvoiced;
  }

  public void setIsInvoiced(String isInvoiced) {
    this.isInvoiced = isInvoiced;
  }


  public Form isShared(Boolean isShared) {
    this.isShared = isShared;
    return this;
  }

  /**
   * Get isShared
   * @return isShared
   */
  @javax.annotation.Nullable
  public Boolean getIsShared() {
    return isShared;
  }

  public void setIsShared(Boolean isShared) {
    this.isShared = isShared;
  }


  public Form massFormId(UUID massFormId) {
    this.massFormId = massFormId;
    return this;
  }

  /**
   * Get massFormId
   * @return massFormId
   */
  @javax.annotation.Nullable
  public UUID getMassFormId() {
    return massFormId;
  }

  public void setMassFormId(UUID massFormId) {
    this.massFormId = massFormId;
  }


  /**
   * Get modified
   * @return modified
   */
  @javax.annotation.Nullable
  public String getModified() {
    return modified;
  }



  public Form projectId(UUID projectId) {
    this.projectId = projectId;
    return this;
  }

  /**
   * Get projectId
   * @return projectId
   */
  @javax.annotation.Nullable
  public UUID getProjectId() {
    return projectId;
  }

  public void setProjectId(UUID projectId) {
    this.projectId = projectId;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Form form = (Form) o;
    return Objects.equals(this.approvedById, form.approvedById) &&
        Objects.equals(this.companyId, form.companyId) &&
        Objects.equals(this.created, form.created) &&
        Objects.equals(this.createdById, form.createdById) &&
        Objects.equals(this.deleted, form.deleted) &&
        Objects.equals(this.formDate, form.formDate) &&
        Objects.equals(this.formTemplateId, form.formTemplateId) &&
        Objects.equals(this.id, form.id) &&
        Objects.equals(this.isDraft, form.isDraft) &&
        Objects.equals(this.isInvoiced, form.isInvoiced) &&
        Objects.equals(this.isShared, form.isShared) &&
        Objects.equals(this.massFormId, form.massFormId) &&
        Objects.equals(this.modified, form.modified) &&
        Objects.equals(this.projectId, form.projectId);
  }

  @Override
  public int hashCode() {
    return Objects.hash(approvedById, companyId, created, createdById, deleted, formDate, formTemplateId, id, isDraft, isInvoiced, isShared, massFormId, modified, projectId);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Form {\n");
    sb.append("    approvedById: ").append(toIndentedString(approvedById)).append("\n");
    sb.append("    companyId: ").append(toIndentedString(companyId)).append("\n");
    sb.append("    created: ").append(toIndentedString(created)).append("\n");
    sb.append("    createdById: ").append(toIndentedString(createdById)).append("\n");
    sb.append("    deleted: ").append(toIndentedString(deleted)).append("\n");
    sb.append("    formDate: ").append(toIndentedString(formDate)).append("\n");
    sb.append("    formTemplateId: ").append(toIndentedString(formTemplateId)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    isDraft: ").append(toIndentedString(isDraft)).append("\n");
    sb.append("    isInvoiced: ").append(toIndentedString(isInvoiced)).append("\n");
    sb.append("    isShared: ").append(toIndentedString(isShared)).append("\n");
    sb.append("    massFormId: ").append(toIndentedString(massFormId)).append("\n");
    sb.append("    modified: ").append(toIndentedString(modified)).append("\n");
    sb.append("    projectId: ").append(toIndentedString(projectId)).append("\n");
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
    openapiFields.add("approved_by_id");
    openapiFields.add("company_id");
    openapiFields.add("created");
    openapiFields.add("created_by_id");
    openapiFields.add("deleted");
    openapiFields.add("form_date");
    openapiFields.add("form_template_id");
    openapiFields.add("id");
    openapiFields.add("is_draft");
    openapiFields.add("is_invoiced");
    openapiFields.add("is_shared");
    openapiFields.add("mass_form_id");
    openapiFields.add("modified");
    openapiFields.add("project_id");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Form
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Form.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Form is not found in the empty JSON string", Form.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Form.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Form` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if ((jsonObj.get("approved_by_id") != null && !jsonObj.get("approved_by_id").isJsonNull()) && !jsonObj.get("approved_by_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `approved_by_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("approved_by_id").toString()));
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
      if ((jsonObj.get("form_template_id") != null && !jsonObj.get("form_template_id").isJsonNull()) && !jsonObj.get("form_template_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `form_template_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("form_template_id").toString()));
      }
      if ((jsonObj.get("id") != null && !jsonObj.get("id").isJsonNull()) && !jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("is_invoiced") != null && !jsonObj.get("is_invoiced").isJsonNull()) && !jsonObj.get("is_invoiced").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `is_invoiced` to be a primitive type in the JSON string but got `%s`", jsonObj.get("is_invoiced").toString()));
      }
      if ((jsonObj.get("mass_form_id") != null && !jsonObj.get("mass_form_id").isJsonNull()) && !jsonObj.get("mass_form_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `mass_form_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("mass_form_id").toString()));
      }
      if ((jsonObj.get("modified") != null && !jsonObj.get("modified").isJsonNull()) && !jsonObj.get("modified").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `modified` to be a primitive type in the JSON string but got `%s`", jsonObj.get("modified").toString()));
      }
      if ((jsonObj.get("project_id") != null && !jsonObj.get("project_id").isJsonNull()) && !jsonObj.get("project_id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `project_id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("project_id").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Form.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Form' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Form> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Form.class));

       return (TypeAdapter<T>) new TypeAdapter<Form>() {
           @Override
           public void write(JsonWriter out, Form value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Form read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Form given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Form
   * @throws IOException if the JSON string is invalid with respect to Form
   */
  public static Form fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Form.class);
  }

  /**
   * Convert an instance of Form to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

