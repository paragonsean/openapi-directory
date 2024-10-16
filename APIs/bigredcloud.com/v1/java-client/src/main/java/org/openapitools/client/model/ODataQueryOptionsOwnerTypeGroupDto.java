/*
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
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
import org.openapitools.client.model.FilterQueryOption;
import org.openapitools.client.model.InlineCountQueryOption;
import org.openapitools.client.model.ODataQueryContext;
import org.openapitools.client.model.ODataRawQueryOptions;
import org.openapitools.client.model.OrderByQueryOption;
import org.openapitools.client.model.SelectExpandQueryOption;
import org.openapitools.client.model.SkipQueryOption;
import org.openapitools.client.model.TopQueryOption;

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
 * ODataQueryOptionsOwnerTypeGroupDto
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:00:05.666566-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ODataQueryOptionsOwnerTypeGroupDto {
  public static final String SERIALIZED_NAME_CONTEXT = "Context";
  @SerializedName(SERIALIZED_NAME_CONTEXT)
  private ODataQueryContext context;

  public static final String SERIALIZED_NAME_FILTER = "Filter";
  @SerializedName(SERIALIZED_NAME_FILTER)
  private FilterQueryOption filter;

  public static final String SERIALIZED_NAME_IF_MATCH = "IfMatch";
  @SerializedName(SERIALIZED_NAME_IF_MATCH)
  private Object ifMatch;

  public static final String SERIALIZED_NAME_IF_NONE_MATCH = "IfNoneMatch";
  @SerializedName(SERIALIZED_NAME_IF_NONE_MATCH)
  private Object ifNoneMatch;

  public static final String SERIALIZED_NAME_INLINE_COUNT = "InlineCount";
  @SerializedName(SERIALIZED_NAME_INLINE_COUNT)
  private InlineCountQueryOption inlineCount;

  public static final String SERIALIZED_NAME_ORDER_BY = "OrderBy";
  @SerializedName(SERIALIZED_NAME_ORDER_BY)
  private OrderByQueryOption orderBy;

  public static final String SERIALIZED_NAME_RAW_VALUES = "RawValues";
  @SerializedName(SERIALIZED_NAME_RAW_VALUES)
  private ODataRawQueryOptions rawValues;

  public static final String SERIALIZED_NAME_REQUEST = "Request";
  @SerializedName(SERIALIZED_NAME_REQUEST)
  private Object request;

  public static final String SERIALIZED_NAME_SELECT_EXPAND = "SelectExpand";
  @SerializedName(SERIALIZED_NAME_SELECT_EXPAND)
  private SelectExpandQueryOption selectExpand;

  public static final String SERIALIZED_NAME_SKIP = "Skip";
  @SerializedName(SERIALIZED_NAME_SKIP)
  private SkipQueryOption skip;

  public static final String SERIALIZED_NAME_TOP = "Top";
  @SerializedName(SERIALIZED_NAME_TOP)
  private TopQueryOption top;

  public static final String SERIALIZED_NAME_VALIDATOR = "Validator";
  @SerializedName(SERIALIZED_NAME_VALIDATOR)
  private Object validator;

  public ODataQueryOptionsOwnerTypeGroupDto() {
  }

  public ODataQueryOptionsOwnerTypeGroupDto(
     Object ifMatch, 
     Object ifNoneMatch, 
     Object request
  ) {
    this();
    this.ifMatch = ifMatch;
    this.ifNoneMatch = ifNoneMatch;
    this.request = request;
  }

  public ODataQueryOptionsOwnerTypeGroupDto context(ODataQueryContext context) {
    this.context = context;
    return this;
  }

  /**
   * Get context
   * @return context
   */
  @javax.annotation.Nullable
  public ODataQueryContext getContext() {
    return context;
  }

  public void setContext(ODataQueryContext context) {
    this.context = context;
  }


  public ODataQueryOptionsOwnerTypeGroupDto filter(FilterQueryOption filter) {
    this.filter = filter;
    return this;
  }

  /**
   * Get filter
   * @return filter
   */
  @javax.annotation.Nullable
  public FilterQueryOption getFilter() {
    return filter;
  }

  public void setFilter(FilterQueryOption filter) {
    this.filter = filter;
  }


  /**
   * Get ifMatch
   * @return ifMatch
   */
  @javax.annotation.Nullable
  public Object getIfMatch() {
    return ifMatch;
  }



  /**
   * Get ifNoneMatch
   * @return ifNoneMatch
   */
  @javax.annotation.Nullable
  public Object getIfNoneMatch() {
    return ifNoneMatch;
  }



  public ODataQueryOptionsOwnerTypeGroupDto inlineCount(InlineCountQueryOption inlineCount) {
    this.inlineCount = inlineCount;
    return this;
  }

  /**
   * Get inlineCount
   * @return inlineCount
   */
  @javax.annotation.Nullable
  public InlineCountQueryOption getInlineCount() {
    return inlineCount;
  }

  public void setInlineCount(InlineCountQueryOption inlineCount) {
    this.inlineCount = inlineCount;
  }


  public ODataQueryOptionsOwnerTypeGroupDto orderBy(OrderByQueryOption orderBy) {
    this.orderBy = orderBy;
    return this;
  }

  /**
   * Get orderBy
   * @return orderBy
   */
  @javax.annotation.Nullable
  public OrderByQueryOption getOrderBy() {
    return orderBy;
  }

  public void setOrderBy(OrderByQueryOption orderBy) {
    this.orderBy = orderBy;
  }


  public ODataQueryOptionsOwnerTypeGroupDto rawValues(ODataRawQueryOptions rawValues) {
    this.rawValues = rawValues;
    return this;
  }

  /**
   * Get rawValues
   * @return rawValues
   */
  @javax.annotation.Nullable
  public ODataRawQueryOptions getRawValues() {
    return rawValues;
  }

  public void setRawValues(ODataRawQueryOptions rawValues) {
    this.rawValues = rawValues;
  }


  /**
   * Get request
   * @return request
   */
  @javax.annotation.Nullable
  public Object getRequest() {
    return request;
  }



  public ODataQueryOptionsOwnerTypeGroupDto selectExpand(SelectExpandQueryOption selectExpand) {
    this.selectExpand = selectExpand;
    return this;
  }

  /**
   * Get selectExpand
   * @return selectExpand
   */
  @javax.annotation.Nullable
  public SelectExpandQueryOption getSelectExpand() {
    return selectExpand;
  }

  public void setSelectExpand(SelectExpandQueryOption selectExpand) {
    this.selectExpand = selectExpand;
  }


  public ODataQueryOptionsOwnerTypeGroupDto skip(SkipQueryOption skip) {
    this.skip = skip;
    return this;
  }

  /**
   * Get skip
   * @return skip
   */
  @javax.annotation.Nullable
  public SkipQueryOption getSkip() {
    return skip;
  }

  public void setSkip(SkipQueryOption skip) {
    this.skip = skip;
  }


  public ODataQueryOptionsOwnerTypeGroupDto top(TopQueryOption top) {
    this.top = top;
    return this;
  }

  /**
   * Get top
   * @return top
   */
  @javax.annotation.Nullable
  public TopQueryOption getTop() {
    return top;
  }

  public void setTop(TopQueryOption top) {
    this.top = top;
  }


  public ODataQueryOptionsOwnerTypeGroupDto validator(Object validator) {
    this.validator = validator;
    return this;
  }

  /**
   * Get validator
   * @return validator
   */
  @javax.annotation.Nullable
  public Object getValidator() {
    return validator;
  }

  public void setValidator(Object validator) {
    this.validator = validator;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ODataQueryOptionsOwnerTypeGroupDto odataQueryOptionsOwnerTypeGroupDto = (ODataQueryOptionsOwnerTypeGroupDto) o;
    return Objects.equals(this.context, odataQueryOptionsOwnerTypeGroupDto.context) &&
        Objects.equals(this.filter, odataQueryOptionsOwnerTypeGroupDto.filter) &&
        Objects.equals(this.ifMatch, odataQueryOptionsOwnerTypeGroupDto.ifMatch) &&
        Objects.equals(this.ifNoneMatch, odataQueryOptionsOwnerTypeGroupDto.ifNoneMatch) &&
        Objects.equals(this.inlineCount, odataQueryOptionsOwnerTypeGroupDto.inlineCount) &&
        Objects.equals(this.orderBy, odataQueryOptionsOwnerTypeGroupDto.orderBy) &&
        Objects.equals(this.rawValues, odataQueryOptionsOwnerTypeGroupDto.rawValues) &&
        Objects.equals(this.request, odataQueryOptionsOwnerTypeGroupDto.request) &&
        Objects.equals(this.selectExpand, odataQueryOptionsOwnerTypeGroupDto.selectExpand) &&
        Objects.equals(this.skip, odataQueryOptionsOwnerTypeGroupDto.skip) &&
        Objects.equals(this.top, odataQueryOptionsOwnerTypeGroupDto.top) &&
        Objects.equals(this.validator, odataQueryOptionsOwnerTypeGroupDto.validator);
  }

  @Override
  public int hashCode() {
    return Objects.hash(context, filter, ifMatch, ifNoneMatch, inlineCount, orderBy, rawValues, request, selectExpand, skip, top, validator);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ODataQueryOptionsOwnerTypeGroupDto {\n");
    sb.append("    context: ").append(toIndentedString(context)).append("\n");
    sb.append("    filter: ").append(toIndentedString(filter)).append("\n");
    sb.append("    ifMatch: ").append(toIndentedString(ifMatch)).append("\n");
    sb.append("    ifNoneMatch: ").append(toIndentedString(ifNoneMatch)).append("\n");
    sb.append("    inlineCount: ").append(toIndentedString(inlineCount)).append("\n");
    sb.append("    orderBy: ").append(toIndentedString(orderBy)).append("\n");
    sb.append("    rawValues: ").append(toIndentedString(rawValues)).append("\n");
    sb.append("    request: ").append(toIndentedString(request)).append("\n");
    sb.append("    selectExpand: ").append(toIndentedString(selectExpand)).append("\n");
    sb.append("    skip: ").append(toIndentedString(skip)).append("\n");
    sb.append("    top: ").append(toIndentedString(top)).append("\n");
    sb.append("    validator: ").append(toIndentedString(validator)).append("\n");
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
    openapiFields.add("Context");
    openapiFields.add("Filter");
    openapiFields.add("IfMatch");
    openapiFields.add("IfNoneMatch");
    openapiFields.add("InlineCount");
    openapiFields.add("OrderBy");
    openapiFields.add("RawValues");
    openapiFields.add("Request");
    openapiFields.add("SelectExpand");
    openapiFields.add("Skip");
    openapiFields.add("Top");
    openapiFields.add("Validator");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ODataQueryOptionsOwnerTypeGroupDto
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ODataQueryOptionsOwnerTypeGroupDto.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ODataQueryOptionsOwnerTypeGroupDto is not found in the empty JSON string", ODataQueryOptionsOwnerTypeGroupDto.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ODataQueryOptionsOwnerTypeGroupDto.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ODataQueryOptionsOwnerTypeGroupDto` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `Context`
      if (jsonObj.get("Context") != null && !jsonObj.get("Context").isJsonNull()) {
        ODataQueryContext.validateJsonElement(jsonObj.get("Context"));
      }
      // validate the optional field `Filter`
      if (jsonObj.get("Filter") != null && !jsonObj.get("Filter").isJsonNull()) {
        FilterQueryOption.validateJsonElement(jsonObj.get("Filter"));
      }
      // validate the optional field `InlineCount`
      if (jsonObj.get("InlineCount") != null && !jsonObj.get("InlineCount").isJsonNull()) {
        InlineCountQueryOption.validateJsonElement(jsonObj.get("InlineCount"));
      }
      // validate the optional field `OrderBy`
      if (jsonObj.get("OrderBy") != null && !jsonObj.get("OrderBy").isJsonNull()) {
        OrderByQueryOption.validateJsonElement(jsonObj.get("OrderBy"));
      }
      // validate the optional field `RawValues`
      if (jsonObj.get("RawValues") != null && !jsonObj.get("RawValues").isJsonNull()) {
        ODataRawQueryOptions.validateJsonElement(jsonObj.get("RawValues"));
      }
      // validate the optional field `SelectExpand`
      if (jsonObj.get("SelectExpand") != null && !jsonObj.get("SelectExpand").isJsonNull()) {
        SelectExpandQueryOption.validateJsonElement(jsonObj.get("SelectExpand"));
      }
      // validate the optional field `Skip`
      if (jsonObj.get("Skip") != null && !jsonObj.get("Skip").isJsonNull()) {
        SkipQueryOption.validateJsonElement(jsonObj.get("Skip"));
      }
      // validate the optional field `Top`
      if (jsonObj.get("Top") != null && !jsonObj.get("Top").isJsonNull()) {
        TopQueryOption.validateJsonElement(jsonObj.get("Top"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ODataQueryOptionsOwnerTypeGroupDto.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ODataQueryOptionsOwnerTypeGroupDto' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ODataQueryOptionsOwnerTypeGroupDto> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ODataQueryOptionsOwnerTypeGroupDto.class));

       return (TypeAdapter<T>) new TypeAdapter<ODataQueryOptionsOwnerTypeGroupDto>() {
           @Override
           public void write(JsonWriter out, ODataQueryOptionsOwnerTypeGroupDto value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ODataQueryOptionsOwnerTypeGroupDto read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ODataQueryOptionsOwnerTypeGroupDto given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ODataQueryOptionsOwnerTypeGroupDto
   * @throws IOException if the JSON string is invalid with respect to ODataQueryOptionsOwnerTypeGroupDto
   */
  public static ODataQueryOptionsOwnerTypeGroupDto fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ODataQueryOptionsOwnerTypeGroupDto.class);
  }

  /**
   * Convert an instance of ODataQueryOptionsOwnerTypeGroupDto to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

