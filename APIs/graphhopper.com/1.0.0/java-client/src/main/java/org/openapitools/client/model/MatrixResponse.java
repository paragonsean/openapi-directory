/*
 * GraphHopper Directions API
 *  With the [GraphHopper Directions API](https://www.graphhopper.com/products/) you can integrate A-to-B route planning, turn-by-turn navigation, route optimization, isochrone calculations and other tools in your application.  The GraphHopper Directions API consists of the following RESTful web services:   * [Routing API](#tag/Routing-API),  * [Route Optimization API](#tag/Route-Optimization-API),  * [Isochrone API](#tag/Isochrone-API),  * [Map Matching API](#tag/Map-Matching-API),  * [Matrix API](#tag/Matrix-API),  * [Geocoding API](#tag/Geocoding-API) and  * [Cluster API](#tag/Cluster-API).  # Explore our APIs  ## Get started  1. [Sign up for GraphHopper](https://support.graphhopper.com/a/solutions/articles/44001976025) 2. [Create an API key](https://support.graphhopper.com/a/solutions/articles/44001976027)  Each API part has its own documentation. Jump to the desired API part and learn about the API through the given examples and tutorials.  In addition, for each API there are specific sample requests that you can send via Insomnia or Postman to see what the requests and responses look like.  ## Insomnia  To explore our APIs with [Insomnia](https://insomnia.rest/), follow these steps:  1. Open Insomnia and Import [our workspace](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/GraphHopper-Direction-API-Insomnia.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your workspace: Manage Environments -> Base Environment -> `\"api_key\": your API key` 3. Start exploring  ![Insomnia](./img/insomnia.png)  ## Postman  To explore our APIs with [Postman](https://www.getpostman.com/), follow these steps:  1. Import our [request collections](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_collection.json) as well as our [environment file](https://raw.githubusercontent.com/graphhopper/directions-api-doc/master/web/restclients/graphhopper_directions_api.postman_environment.json). 2. Specify [your API key](https://graphhopper.com/dashboard/#/register) in your environment: `\"api_key\": your API key` 3. Start exploring  ![Postman](./img/postman.png)  ## API Client Libraries  To speed up development and make coding easier, we offer the following client libraries:   * [JavaScript client](https://github.com/graphhopper/directions-api-js-client) - try the [live examples](https://graphhopper.com/api/1/examples/)  * [Others](https://github.com/graphhopper/directions-api-clients) like C#, Ruby, PHP, Python, ... automatically created for the Route Optimization API  ### Bandwidth reduction  If you create your own client, make sure it supports http/2 and gzipped responses for best speed.  If you use the Matrix, the Route Optimization API or the Cluster API and want to solve large problems, we recommend you to reduce bandwidth by [compressing your POST request](https://gist.github.com/karussell/82851e303ea7b3459b2dea01f18949f4) and specifying the header as follows: `Content-Encoding: gzip`. This will also avoid the HTTP 413 error \"Request Entity Too Large\".  ## Contact Us  If you have problems or questions, please read the following information:  - [FAQ](https://graphhopper.com/api/1/docs/FAQ/) - [Public forum](https://discuss.graphhopper.com/c/directions-api) - [Contact us](https://www.graphhopper.com/contact-form/) - [GraphHopper Status Page](https://status.graphhopper.com/)  To stay informed about the latest developments, you can  - follow us on [twitter](https://twitter.com/graphhopper/), - read [our blog](https://graphhopper.com/blog/), - watch [our documentation repository](https://github.com/graphhopper/directions-api-doc), - sign up for our newsletter or - [our forum](https://discuss.graphhopper.com/c/directions-api).  Select the channel you like the most.   # Map Data and Routing Profiles  Currently, our main data source is [OpenStreetMap](https://www.openstreetmap.org). We also integrated other network data providers. This chapter gives an overview about the options you have.  ## OpenStreetMap  #### Geographical Coverage  [OpenStreetMap](https://www.openstreetmap.org) covers the whole world. If you want to see for yourself if we can provide data suitable for your region, please visit [GraphHopper Maps](https://graphhopper.com/maps/). You can edit and modify OpenStreetMap data if you find that important information is missing, e.g. a weight limit for a bridge. [Here](https://wiki.openstreetmap.org/wiki/Beginners%27_guide) is a beginner's guide that shows how to add data. If you have edited data, we usually consider your data after 1 week at the latest.  #### Supported Vehicle Profiles  The Routing, Matrix and Route Optimization APIs support the following vehicle profiles:  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) truck      | Truck like a MAN or Mercedes-Benz Actros | height=3.7m, width=2.6+0.5m, length=12m, weight=13000 + 13000 kg, hgv=yes, 3 Axes | ![truck image](https://graphhopper.com/maps/img/truck.png) scooter    | Moped mode | Fast inner city, often used for food delivery, is able to ignore certain bollards, maximum speed of roughly 50km/h | ![scooter image](https://graphhopper.com/maps/img/scooter.png) foot       | Pedestrian or walking without dangerous [SAC-scales](https://wiki.openstreetmap.org/wiki/Key:sac_scale) | foot access         | ![foot image](https://graphhopper.com/maps/img/foot.png) hike       | Pedestrian or walking with priority for more beautiful hiking tours and potentially a bit longer than `foot`. Walking duration is influenced by elevation differences.  | foot access         | ![hike image](https://graphhopper.com/maps/img/hike.png) bike       | Trekking bike avoiding hills | bike access  | ![bike image](https://graphhopper.com/maps/img/bike.png) mtb        | Mountainbike          | bike access         | ![Mountainbike image](https://graphhopper.com/maps/img/mtb.png) racingbike| Bike preferring roads | bike access         | ![racingbike image](https://graphhopper.com/maps/img/racingbike.png)  Please note:   * all motor vehicles (`car`, `small_truck`, `truck` and `scooter`) support turn restrictions via `turn_costs=true`  * the free package supports only the vehicle profiles `car`, `bike` or `foot`  * up to 2 different vehicle profiles can be used in a single optimization request. The number of vehicles is unaffected and depends on your subscription.  * we offer custom vehicle profiles with different properties, different speed profiles or different access options. To find out more about custom profiles, please [contact us](https://www.graphhopper.com/contact-form/).  * a sophisticated `motorcycle` profile is available up on request. It is powered by the [Kurviger](https://kurviger.de/en) Routing API and favors curves and slopes while avoiding cities and highways.   ## TomTom  If you want to include traffic, you can purchase the TomTom Add-on. This Add-on only uses TomTom's road network and historical traffic information. Live traffic is not yet considered. If you are interested to learn how we consider traffic information, we recommend that you read [this article](https://www.graphhopper.com/blog/2017/11/06/time-dependent-optimization/).  Please note the following:   * Currently we only offer this for our [Route Optimization API](#tag/Route-Optimization-API).  * In addition to our terms, you need to accept TomTom's [End User License Aggreement](https://www.graphhopper.com/tomtom-end-user-license-agreement/).  * We do *not* use TomTom's web services. We only use their data with our software.   [Contact us](https://www.graphhopper.com/contact-form/) for more details.  #### Geographical Coverage  We offer  - Europe including Russia - North, Central and South America - Saudi Arabia - United Arab Emirates - South Africa - Australia  #### Supported Vehicle Profiles  Name       | Description           | Restrictions              | Icon -----------|:----------------------|:--------------------------|:--------------------------------------------------------- car        | Car mode              | car access                | ![car image](https://graphhopper.com/maps/img/car.png) small_truck| Small truck like a Mercedes Sprinter, Ford Transit or Iveco Daily | height=2.7m, width=2+0.4m, length=5.5m, weight=2080+1400 kg | ![small truck image](https://graphhopper.com/maps/img/small_truck.png) 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@graphhopper.com
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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.MatrixResponseHintsInner;
import org.openapitools.client.model.ResponseInfo;

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
 * MatrixResponse
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class MatrixResponse {
  public static final String SERIALIZED_NAME_DISTANCES = "distances";
  @SerializedName(SERIALIZED_NAME_DISTANCES)
  private List<List<BigDecimal>> distances = new ArrayList<>();

  public static final String SERIALIZED_NAME_HINTS = "hints";
  @SerializedName(SERIALIZED_NAME_HINTS)
  private List<MatrixResponseHintsInner> hints = new ArrayList<>();

  public static final String SERIALIZED_NAME_INFO = "info";
  @SerializedName(SERIALIZED_NAME_INFO)
  private ResponseInfo info;

  public static final String SERIALIZED_NAME_TIMES = "times";
  @SerializedName(SERIALIZED_NAME_TIMES)
  private List<List<BigDecimal>> times = new ArrayList<>();

  public static final String SERIALIZED_NAME_WEIGHTS = "weights";
  @SerializedName(SERIALIZED_NAME_WEIGHTS)
  private List<List<Double>> weights = new ArrayList<>();

  public MatrixResponse() {
  }

  public MatrixResponse distances(List<List<BigDecimal>> distances) {
    this.distances = distances;
    return this;
  }

  public MatrixResponse addDistancesItem(List<BigDecimal> distancesItem) {
    if (this.distances == null) {
      this.distances = new ArrayList<>();
    }
    this.distances.add(distancesItem);
    return this;
  }

  /**
   * The distance matrix for the specified points in the same order as the time matrix. The distances are in meters. If &#x60;fail_fast&#x3D;false&#x60; the matrix will contain &#x60;null&#x60; for connections that could not be found.
   * @return distances
   */
  @javax.annotation.Nullable
  public List<List<BigDecimal>> getDistances() {
    return distances;
  }

  public void setDistances(List<List<BigDecimal>> distances) {
    this.distances = distances;
  }


  public MatrixResponse hints(List<MatrixResponseHintsInner> hints) {
    this.hints = hints;
    return this;
  }

  public MatrixResponse addHintsItem(MatrixResponseHintsInner hintsItem) {
    if (this.hints == null) {
      this.hints = new ArrayList<>();
    }
    this.hints.add(hintsItem);
    return this;
  }

  /**
   * Optional. Additional response data.
   * @return hints
   */
  @javax.annotation.Nullable
  public List<MatrixResponseHintsInner> getHints() {
    return hints;
  }

  public void setHints(List<MatrixResponseHintsInner> hints) {
    this.hints = hints;
  }


  public MatrixResponse info(ResponseInfo info) {
    this.info = info;
    return this;
  }

  /**
   * Get info
   * @return info
   */
  @javax.annotation.Nullable
  public ResponseInfo getInfo() {
    return info;
  }

  public void setInfo(ResponseInfo info) {
    this.info = info;
  }


  public MatrixResponse times(List<List<BigDecimal>> times) {
    this.times = times;
    return this;
  }

  public MatrixResponse addTimesItem(List<BigDecimal> timesItem) {
    if (this.times == null) {
      this.times = new ArrayList<>();
    }
    this.times.add(timesItem);
    return this;
  }

  /**
   * The time matrix for the specified points in the order [[from1-&gt;to1, from1-&gt;to2, ...], [from2-&gt;to1, from2-&gt;to2, ...], ...]. The times are in seconds. If &#x60;fail_fast&#x3D;false&#x60; the matrix will contain &#x60;null&#x60; for connections that could not be found.
   * @return times
   */
  @javax.annotation.Nullable
  public List<List<BigDecimal>> getTimes() {
    return times;
  }

  public void setTimes(List<List<BigDecimal>> times) {
    this.times = times;
  }


  public MatrixResponse weights(List<List<Double>> weights) {
    this.weights = weights;
    return this;
  }

  public MatrixResponse addWeightsItem(List<Double> weightsItem) {
    if (this.weights == null) {
      this.weights = new ArrayList<>();
    }
    this.weights.add(weightsItem);
    return this;
  }

  /**
   * The weight matrix for the specified points in the same order as the time matrix. The weights for different vehicles can have a different unit but the weights array is perfectly suited as input for Vehicle Routing Problems as it is currently faster to calculate. If &#x60;fail_fast&#x3D;false&#x60; the matrix will contain &#x60;null&#x60; for connections that could not be found.
   * @return weights
   */
  @javax.annotation.Nullable
  public List<List<Double>> getWeights() {
    return weights;
  }

  public void setWeights(List<List<Double>> weights) {
    this.weights = weights;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    MatrixResponse matrixResponse = (MatrixResponse) o;
    return Objects.equals(this.distances, matrixResponse.distances) &&
        Objects.equals(this.hints, matrixResponse.hints) &&
        Objects.equals(this.info, matrixResponse.info) &&
        Objects.equals(this.times, matrixResponse.times) &&
        Objects.equals(this.weights, matrixResponse.weights);
  }

  @Override
  public int hashCode() {
    return Objects.hash(distances, hints, info, times, weights);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class MatrixResponse {\n");
    sb.append("    distances: ").append(toIndentedString(distances)).append("\n");
    sb.append("    hints: ").append(toIndentedString(hints)).append("\n");
    sb.append("    info: ").append(toIndentedString(info)).append("\n");
    sb.append("    times: ").append(toIndentedString(times)).append("\n");
    sb.append("    weights: ").append(toIndentedString(weights)).append("\n");
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
    openapiFields.add("distances");
    openapiFields.add("hints");
    openapiFields.add("info");
    openapiFields.add("times");
    openapiFields.add("weights");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to MatrixResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!MatrixResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in MatrixResponse is not found in the empty JSON string", MatrixResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!MatrixResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `MatrixResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("distances") != null && !jsonObj.get("distances").isJsonNull() && !jsonObj.get("distances").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `distances` to be an array in the JSON string but got `%s`", jsonObj.get("distances").toString()));
      }
      if (jsonObj.get("hints") != null && !jsonObj.get("hints").isJsonNull()) {
        JsonArray jsonArrayhints = jsonObj.getAsJsonArray("hints");
        if (jsonArrayhints != null) {
          // ensure the json data is an array
          if (!jsonObj.get("hints").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `hints` to be an array in the JSON string but got `%s`", jsonObj.get("hints").toString()));
          }

          // validate the optional field `hints` (array)
          for (int i = 0; i < jsonArrayhints.size(); i++) {
            MatrixResponseHintsInner.validateJsonElement(jsonArrayhints.get(i));
          };
        }
      }
      // validate the optional field `info`
      if (jsonObj.get("info") != null && !jsonObj.get("info").isJsonNull()) {
        ResponseInfo.validateJsonElement(jsonObj.get("info"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("times") != null && !jsonObj.get("times").isJsonNull() && !jsonObj.get("times").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `times` to be an array in the JSON string but got `%s`", jsonObj.get("times").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("weights") != null && !jsonObj.get("weights").isJsonNull() && !jsonObj.get("weights").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `weights` to be an array in the JSON string but got `%s`", jsonObj.get("weights").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!MatrixResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'MatrixResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<MatrixResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(MatrixResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<MatrixResponse>() {
           @Override
           public void write(JsonWriter out, MatrixResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public MatrixResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of MatrixResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of MatrixResponse
   * @throws IOException if the JSON string is invalid with respect to MatrixResponse
   */
  public static MatrixResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, MatrixResponse.class);
  }

  /**
   * Convert an instance of MatrixResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

