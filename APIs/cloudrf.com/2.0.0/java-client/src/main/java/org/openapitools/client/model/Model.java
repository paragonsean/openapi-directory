/*
 * Cloud-RF API
 * Use this JSON API to build and test radio links for any radio, anywhere. Authenticate with your API2.0 key in the request header as key
 *
 * The version of the OpenAPI document: 2.0.0
 * Contact: support@cloudrf.com
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
 * Model
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:22.355657-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Model {
  public static final String SERIALIZED_NAME_CLI = "cli";
  @SerializedName(SERIALIZED_NAME_CLI)
  private Integer cli = 6;

  public static final String SERIALIZED_NAME_KED = "ked";
  @SerializedName(SERIALIZED_NAME_KED)
  private Integer ked = 0;

  public static final String SERIALIZED_NAME_PE = "pe";
  @SerializedName(SERIALIZED_NAME_PE)
  private Integer pe = 2;

  public static final String SERIALIZED_NAME_PM = "pm";
  @SerializedName(SERIALIZED_NAME_PM)
  private Integer pm = 1;

  public static final String SERIALIZED_NAME_REL = "rel";
  @SerializedName(SERIALIZED_NAME_REL)
  private Integer rel = 95;

  public static final String SERIALIZED_NAME_TER = "ter";
  @SerializedName(SERIALIZED_NAME_TER)
  private Integer ter = 4;

  public Model() {
  }

  public Model cli(Integer cli) {
    this.cli = cli;
    return this;
  }

  /**
   * Radio climate for ITM model (1). 1: Equatorial (Congo) 2: Continental Subtropical (Sudan) 3: Maritime Subtropical (West coast of Africa) 4: Desert (Sahara) 5: Continental Temperate 6: Maritime Temperate, over land (UK and west coasts of US &amp; EU) 7: Maritime Temperate, over sea
   * minimum: 1
   * maximum: 7
   * @return cli
   */
  @javax.annotation.Nullable
  public Integer getCli() {
    return cli;
  }

  public void setCli(Integer cli) {
    this.cli = cli;
  }


  public Model ked(Integer ked) {
    this.ked = ked;
    return this;
  }

  /**
   * Knife edge diffraction for enhancing basic empirical models (Already in ITM)
   * minimum: 0
   * maximum: 1
   * @return ked
   */
  @javax.annotation.Nullable
  public Integer getKed() {
    return ked;
  }

  public void setKed(Integer ked) {
    this.ked = ked;
  }


  public Model pe(Integer pe) {
    this.pe = pe;
    return this;
  }

  /**
   * Propagation model subtype/environment. 1&#x3D;Conservative/Urban,2&#x3D;Average/Suburban,3&#x3D;Optimistic/rural
   * minimum: 1
   * maximum: 3
   * @return pe
   */
  @javax.annotation.Nullable
  public Integer getPe() {
    return pe;
  }

  public void setPe(Integer pe) {
    this.pe = pe;
  }


  public Model pm(Integer pm) {
    this.pm = pm;
    return this;
  }

  /**
   * Propagation model. 1&#x3D;Irregular Terrain Model, 2&#x3D;Line of Sight (LOS), 3&#x3D;Hata, 4&#x3D;ECC33, 5&#x3D;SUI Microwave, 6&#x3D;COST231, 7&#x3D;Free space path loss, 9&#x3D;Ericsson9999, 10&#x3D;Plane earth loss, 11&#x3D;Egli.
   * minimum: 1
   * maximum: 20
   * @return pm
   */
  @javax.annotation.Nullable
  public Integer getPm() {
    return pm;
  }

  public void setPm(Integer pm) {
    this.pm = pm;
  }


  public Model rel(Integer rel) {
    this.rel = rel;
    return this;
  }

  /**
   * ITM model required reliability as %
   * minimum: 50
   * maximum: 99
   * @return rel
   */
  @javax.annotation.Nullable
  public Integer getRel() {
    return rel;
  }

  public void setRel(Integer rel) {
    this.rel = rel;
  }


  public Model ter(Integer ter) {
    this.ter = ter;
    return this;
  }

  /**
   * Terrain code for ITM model (1). 1&#x3D;Water,2&#x3D;Wet ground,3&#x3D;Farmland,4&#x3D;Forest/Average,5&#x3D;Mountain/Sand,6&#x3D;City/Poor ground
   * minimum: 1
   * maximum: 6
   * @return ter
   */
  @javax.annotation.Nullable
  public Integer getTer() {
    return ter;
  }

  public void setTer(Integer ter) {
    this.ter = ter;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Model model = (Model) o;
    return Objects.equals(this.cli, model.cli) &&
        Objects.equals(this.ked, model.ked) &&
        Objects.equals(this.pe, model.pe) &&
        Objects.equals(this.pm, model.pm) &&
        Objects.equals(this.rel, model.rel) &&
        Objects.equals(this.ter, model.ter);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cli, ked, pe, pm, rel, ter);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Model {\n");
    sb.append("    cli: ").append(toIndentedString(cli)).append("\n");
    sb.append("    ked: ").append(toIndentedString(ked)).append("\n");
    sb.append("    pe: ").append(toIndentedString(pe)).append("\n");
    sb.append("    pm: ").append(toIndentedString(pm)).append("\n");
    sb.append("    rel: ").append(toIndentedString(rel)).append("\n");
    sb.append("    ter: ").append(toIndentedString(ter)).append("\n");
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
    openapiFields.add("cli");
    openapiFields.add("ked");
    openapiFields.add("pe");
    openapiFields.add("pm");
    openapiFields.add("rel");
    openapiFields.add("ter");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Model
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Model.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Model is not found in the empty JSON string", Model.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Model.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Model` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Model.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Model' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Model> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Model.class));

       return (TypeAdapter<T>) new TypeAdapter<Model>() {
           @Override
           public void write(JsonWriter out, Model value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Model read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Model given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Model
   * @throws IOException if the JSON string is invalid with respect to Model
   */
  public static Model fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Model.class);
  }

  /**
   * Convert an instance of Model to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

