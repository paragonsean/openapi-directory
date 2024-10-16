/*
 * OnSched Consumer API
 * Build secure and scalable custom apps for Online Booking. Our flexible API provides many options for availability and booking.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.BookingFieldViewModel;
import org.openapitools.jackson.nullable.JsonNullable;

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
 * BookingFieldListViewModel
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:59:57.922898-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class BookingFieldListViewModel {
  public static final String SERIALIZED_NAME_BOOKING_FIELDS = "bookingFields";
  @SerializedName(SERIALIZED_NAME_BOOKING_FIELDS)
  private List<BookingFieldViewModel> bookingFields;

  public static final String SERIALIZED_NAME_OBJECT = "object";
  @SerializedName(SERIALIZED_NAME_OBJECT)
  private String _object;

  public static final String SERIALIZED_NAME_TOTAL = "total";
  @SerializedName(SERIALIZED_NAME_TOTAL)
  private Integer total;

  public BookingFieldListViewModel() {
  }

  public BookingFieldListViewModel bookingFields(List<BookingFieldViewModel> bookingFields) {
    this.bookingFields = bookingFields;
    return this;
  }

  public BookingFieldListViewModel addBookingFieldsItem(BookingFieldViewModel bookingFieldsItem) {
    if (this.bookingFields == null) {
      this.bookingFields = new ArrayList<>();
    }
    this.bookingFields.add(bookingFieldsItem);
    return this;
  }

  /**
   * Get bookingFields
   * @return bookingFields
   */
  @javax.annotation.Nullable
  public List<BookingFieldViewModel> getBookingFields() {
    return bookingFields;
  }

  public void setBookingFields(List<BookingFieldViewModel> bookingFields) {
    this.bookingFields = bookingFields;
  }


  public BookingFieldListViewModel _object(String _object) {
    this._object = _object;
    return this;
  }

  /**
   * Get _object
   * @return _object
   */
  @javax.annotation.Nullable
  public String getObject() {
    return _object;
  }

  public void setObject(String _object) {
    this._object = _object;
  }


  public BookingFieldListViewModel total(Integer total) {
    this.total = total;
    return this;
  }

  /**
   * Get total
   * @return total
   */
  @javax.annotation.Nullable
  public Integer getTotal() {
    return total;
  }

  public void setTotal(Integer total) {
    this.total = total;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BookingFieldListViewModel bookingFieldListViewModel = (BookingFieldListViewModel) o;
    return Objects.equals(this.bookingFields, bookingFieldListViewModel.bookingFields) &&
        Objects.equals(this._object, bookingFieldListViewModel._object) &&
        Objects.equals(this.total, bookingFieldListViewModel.total);
  }

  private static <T> boolean equalsNullable(JsonNullable<T> a, JsonNullable<T> b) {
    return a == b || (a != null && b != null && a.isPresent() && b.isPresent() && Objects.deepEquals(a.get(), b.get()));
  }

  @Override
  public int hashCode() {
    return Objects.hash(bookingFields, _object, total);
  }

  private static <T> int hashCodeNullable(JsonNullable<T> a) {
    if (a == null) {
      return 1;
    }
    return a.isPresent() ? Arrays.deepHashCode(new Object[]{a.get()}) : 31;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BookingFieldListViewModel {\n");
    sb.append("    bookingFields: ").append(toIndentedString(bookingFields)).append("\n");
    sb.append("    _object: ").append(toIndentedString(_object)).append("\n");
    sb.append("    total: ").append(toIndentedString(total)).append("\n");
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
    openapiFields.add("bookingFields");
    openapiFields.add("object");
    openapiFields.add("total");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to BookingFieldListViewModel
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!BookingFieldListViewModel.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in BookingFieldListViewModel is not found in the empty JSON string", BookingFieldListViewModel.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!BookingFieldListViewModel.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `BookingFieldListViewModel` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      if (jsonObj.get("bookingFields") != null && !jsonObj.get("bookingFields").isJsonNull()) {
        JsonArray jsonArraybookingFields = jsonObj.getAsJsonArray("bookingFields");
        if (jsonArraybookingFields != null) {
          // ensure the json data is an array
          if (!jsonObj.get("bookingFields").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `bookingFields` to be an array in the JSON string but got `%s`", jsonObj.get("bookingFields").toString()));
          }

          // validate the optional field `bookingFields` (array)
          for (int i = 0; i < jsonArraybookingFields.size(); i++) {
            BookingFieldViewModel.validateJsonElement(jsonArraybookingFields.get(i));
          };
        }
      }
      if ((jsonObj.get("object") != null && !jsonObj.get("object").isJsonNull()) && !jsonObj.get("object").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `object` to be a primitive type in the JSON string but got `%s`", jsonObj.get("object").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!BookingFieldListViewModel.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'BookingFieldListViewModel' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<BookingFieldListViewModel> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(BookingFieldListViewModel.class));

       return (TypeAdapter<T>) new TypeAdapter<BookingFieldListViewModel>() {
           @Override
           public void write(JsonWriter out, BookingFieldListViewModel value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public BookingFieldListViewModel read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of BookingFieldListViewModel given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of BookingFieldListViewModel
   * @throws IOException if the JSON string is invalid with respect to BookingFieldListViewModel
   */
  public static BookingFieldListViewModel fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, BookingFieldListViewModel.class);
  }

  /**
   * Convert an instance of BookingFieldListViewModel to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

