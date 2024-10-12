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
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.Address;
import org.openapitools.client.model.TimeWindow;

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
 * Service
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:20.208084-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Service {
  public static final String SERIALIZED_NAME_ADDRESS = "address";
  @SerializedName(SERIALIZED_NAME_ADDRESS)
  private Address address;

  public static final String SERIALIZED_NAME_ALLOWED_VEHICLES = "allowed_vehicles";
  @SerializedName(SERIALIZED_NAME_ALLOWED_VEHICLES)
  private List<String> allowedVehicles = new ArrayList<>();

  public static final String SERIALIZED_NAME_DISALLOWED_VEHICLES = "disallowed_vehicles";
  @SerializedName(SERIALIZED_NAME_DISALLOWED_VEHICLES)
  private List<String> disallowedVehicles = new ArrayList<>();

  public static final String SERIALIZED_NAME_DURATION = "duration";
  @SerializedName(SERIALIZED_NAME_DURATION)
  private Long duration = 0l;

  public static final String SERIALIZED_NAME_GROUP = "group";
  @SerializedName(SERIALIZED_NAME_GROUP)
  private String group;

  public static final String SERIALIZED_NAME_ID = "id";
  @SerializedName(SERIALIZED_NAME_ID)
  private String id;

  public static final String SERIALIZED_NAME_MAX_TIME_IN_VEHICLE = "max_time_in_vehicle";
  @SerializedName(SERIALIZED_NAME_MAX_TIME_IN_VEHICLE)
  private Long maxTimeInVehicle;

  public static final String SERIALIZED_NAME_NAME = "name";
  @SerializedName(SERIALIZED_NAME_NAME)
  private String name;

  public static final String SERIALIZED_NAME_PREPARATION_TIME = "preparation_time";
  @SerializedName(SERIALIZED_NAME_PREPARATION_TIME)
  private Long preparationTime = 0l;

  public static final String SERIALIZED_NAME_PRIORITY = "priority";
  @SerializedName(SERIALIZED_NAME_PRIORITY)
  private Integer priority = 2;

  public static final String SERIALIZED_NAME_REQUIRED_SKILLS = "required_skills";
  @SerializedName(SERIALIZED_NAME_REQUIRED_SKILLS)
  private List<String> requiredSkills = new ArrayList<>();

  public static final String SERIALIZED_NAME_SIZE = "size";
  @SerializedName(SERIALIZED_NAME_SIZE)
  private List<Integer> size = new ArrayList<>(Arrays.asList(0));

  public static final String SERIALIZED_NAME_TIME_WINDOWS = "time_windows";
  @SerializedName(SERIALIZED_NAME_TIME_WINDOWS)
  private List<TimeWindow> timeWindows = new ArrayList<>();

  /**
   * Specifies type of service. This makes a difference if items are loaded or unloaded, i.e. if one of the size dimensions &gt; 0. If it is specified as &#x60;service&#x60; or &#x60;pickup&#x60;, items are loaded and will stay in the vehicle for the rest of the route (and thus consumes capacity for the rest of the route). If it is a &#x60;delivery&#x60;, items are implicitly loaded at the beginning of the route and will stay in the route until delivery (and thus releases capacity for the rest of the route).
   */
  @JsonAdapter(TypeEnum.Adapter.class)
  public enum TypeEnum {
    SERVICE("service"),
    
    PICKUP("pickup"),
    
    DELIVERY("delivery");

    private String value;

    TypeEnum(String value) {
      this.value = value;
    }

    public String getValue() {
      return value;
    }

    @Override
    public String toString() {
      return String.valueOf(value);
    }

    public static TypeEnum fromValue(String value) {
      for (TypeEnum b : TypeEnum.values()) {
        if (b.value.equals(value)) {
          return b;
        }
      }
      throw new IllegalArgumentException("Unexpected value '" + value + "'");
    }

    public static class Adapter extends TypeAdapter<TypeEnum> {
      @Override
      public void write(final JsonWriter jsonWriter, final TypeEnum enumeration) throws IOException {
        jsonWriter.value(enumeration.getValue());
      }

      @Override
      public TypeEnum read(final JsonReader jsonReader) throws IOException {
        String value =  jsonReader.nextString();
        return TypeEnum.fromValue(value);
      }
    }

    public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      String value = jsonElement.getAsString();
      TypeEnum.fromValue(value);
    }
  }

  public static final String SERIALIZED_NAME_TYPE = "type";
  @SerializedName(SERIALIZED_NAME_TYPE)
  private TypeEnum type = TypeEnum.SERVICE;

  public Service() {
  }

  public Service address(Address address) {
    this.address = address;
    return this;
  }

  /**
   * Get address
   * @return address
   */
  @javax.annotation.Nullable
  public Address getAddress() {
    return address;
  }

  public void setAddress(Address address) {
    this.address = address;
  }


  public Service allowedVehicles(List<String> allowedVehicles) {
    this.allowedVehicles = allowedVehicles;
    return this;
  }

  public Service addAllowedVehiclesItem(String allowedVehiclesItem) {
    if (this.allowedVehicles == null) {
      this.allowedVehicles = new ArrayList<>();
    }
    this.allowedVehicles.add(allowedVehiclesItem);
    return this;
  }

  /**
   * Specifies an array of allowed vehicles, i.e. array of vehicle ids. For example, if this service can only be conducted EITHER by &#x60;technician_peter&#x60; OR &#x60;technician_stefan&#x60; specify this as follows: &#x60;[\&quot;technician_peter\&quot;,\&quot;technician_stefan\&quot;]&#x60;.
   * @return allowedVehicles
   */
  @javax.annotation.Nullable
  public List<String> getAllowedVehicles() {
    return allowedVehicles;
  }

  public void setAllowedVehicles(List<String> allowedVehicles) {
    this.allowedVehicles = allowedVehicles;
  }


  public Service disallowedVehicles(List<String> disallowedVehicles) {
    this.disallowedVehicles = disallowedVehicles;
    return this;
  }

  public Service addDisallowedVehiclesItem(String disallowedVehiclesItem) {
    if (this.disallowedVehicles == null) {
      this.disallowedVehicles = new ArrayList<>();
    }
    this.disallowedVehicles.add(disallowedVehiclesItem);
    return this;
  }

  /**
   * Specifies an array of disallowed vehicles, i.e. array of vehicle ids.
   * @return disallowedVehicles
   */
  @javax.annotation.Nullable
  public List<String> getDisallowedVehicles() {
    return disallowedVehicles;
  }

  public void setDisallowedVehicles(List<String> disallowedVehicles) {
    this.disallowedVehicles = disallowedVehicles;
  }


  public Service duration(Long duration) {
    this.duration = duration;
    return this;
  }

  /**
   * Specifies the duration of the service in seconds, i.e. how long it takes at the customer site.
   * minimum: 0
   * maximum: 604800
   * @return duration
   */
  @javax.annotation.Nullable
  public Long getDuration() {
    return duration;
  }

  public void setDuration(Long duration) {
    this.duration = duration;
  }


  public Service group(String group) {
    this.group = group;
    return this;
  }

  /**
   * Group this service belongs to. See the group relation and [this post](https://discuss.graphhopper.com/t/4040) on how to utilize this.
   * @return group
   */
  @javax.annotation.Nullable
  public String getGroup() {
    return group;
  }

  public void setGroup(String group) {
    this.group = group;
  }


  public Service id(String id) {
    this.id = id;
    return this;
  }

  /**
   * Specifies the id of the service. Ids need to be unique so there must not be two services/shipments with the same id.
   * @return id
   */
  @javax.annotation.Nonnull
  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }


  public Service maxTimeInVehicle(Long maxTimeInVehicle) {
    this.maxTimeInVehicle = maxTimeInVehicle;
    return this;
  }

  /**
   * Specifies the maximum time in seconds a delivery can stay in the vehicle. Currently, it only works with services of \&quot;type\&quot;:\&quot;delivery\&quot;.
   * @return maxTimeInVehicle
   */
  @javax.annotation.Nullable
  public Long getMaxTimeInVehicle() {
    return maxTimeInVehicle;
  }

  public void setMaxTimeInVehicle(Long maxTimeInVehicle) {
    this.maxTimeInVehicle = maxTimeInVehicle;
  }


  public Service name(String name) {
    this.name = name;
    return this;
  }

  /**
   * Meaningful name for service, e.g. &#x60;\&quot;deliver pizza\&quot;&#x60;.
   * @return name
   */
  @javax.annotation.Nullable
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  public Service preparationTime(Long preparationTime) {
    this.preparationTime = preparationTime;
    return this;
  }

  /**
   * Specifies the preparation time in seconds. It can be used to model parking lot search time since if you have 3 identical locations in a row, it only falls due once.
   * minimum: 0
   * maximum: 604800
   * @return preparationTime
   */
  @javax.annotation.Nullable
  public Long getPreparationTime() {
    return preparationTime;
  }

  public void setPreparationTime(Long preparationTime) {
    this.preparationTime = preparationTime;
  }


  public Service priority(Integer priority) {
    this.priority = priority;
    return this;
  }

  /**
   * Specifies the priority. Can be 1 &#x3D; high priority to 10 &#x3D; low priority. Often there are more services/shipments than the available vehicle fleet can handle. Then you can set priorities to differentiate high priority tasks from those that could be left unassigned. I.e. the lower the priority the earlier these tasks are omitted in the solution.
   * @return priority
   */
  @javax.annotation.Nullable
  public Integer getPriority() {
    return priority;
  }

  public void setPriority(Integer priority) {
    this.priority = priority;
  }


  public Service requiredSkills(List<String> requiredSkills) {
    this.requiredSkills = requiredSkills;
    return this;
  }

  public Service addRequiredSkillsItem(String requiredSkillsItem) {
    if (this.requiredSkills == null) {
      this.requiredSkills = new ArrayList<>();
    }
    this.requiredSkills.add(requiredSkillsItem);
    return this;
  }

  /**
   * Specifies an array of required skills, i.e. array of string (not case sensitive). For example, if this service needs to be conducted by a technician having a &#x60;drilling_machine&#x60; and a &#x60;screw_driver&#x60; then specify the array as follows: &#x60;[\&quot;drilling_machine\&quot;,\&quot;screw_driver\&quot;]&#x60;. This means that the service can only be done by a vehicle (technician) that has the skills &#x60;drilling_machine&#x60; AND &#x60;screw_driver&#x60; in its skill array. Otherwise it remains unassigned.
   * @return requiredSkills
   */
  @javax.annotation.Nullable
  public List<String> getRequiredSkills() {
    return requiredSkills;
  }

  public void setRequiredSkills(List<String> requiredSkills) {
    this.requiredSkills = requiredSkills;
  }


  public Service size(List<Integer> size) {
    this.size = size;
    return this;
  }

  public Service addSizeItem(Integer sizeItem) {
    if (this.size == null) {
      this.size = new ArrayList<>(Arrays.asList(0));
    }
    this.size.add(sizeItem);
    return this;
  }

  /**
   * Size can have multiple dimensions and should be in line with the capacity dimension array of the vehicle type. For example, if the item that needs to be delivered has two size dimension, volume and weight, then specify it as follow [ 20, 5 ] assuming a volume of 20 and a weight of 5.
   * @return size
   */
  @javax.annotation.Nullable
  public List<Integer> getSize() {
    return size;
  }

  public void setSize(List<Integer> size) {
    this.size = size;
  }


  public Service timeWindows(List<TimeWindow> timeWindows) {
    this.timeWindows = timeWindows;
    return this;
  }

  public Service addTimeWindowsItem(TimeWindow timeWindowsItem) {
    if (this.timeWindows == null) {
      this.timeWindows = new ArrayList<>();
    }
    this.timeWindows.add(timeWindowsItem);
    return this;
  }

  /**
   * Specifies an array of time window objects (see time_window object below). Specify the time either with the recommended Unix time stamp (the number of seconds since 1970-01-01) or you can also count the seconds relative to Monday morning 00:00 and define the whole week in seconds. For example, Monday 9am is then represented by 9hour * 3600sec/hour &#x3D; 32400. In turn, Wednesday 1pm corresponds to 2day * 24hour/day * 3600sec/hour + 1day * 13hour/day * 3600sec/hour &#x3D; 219600. See this tutorial for more information.
   * @return timeWindows
   */
  @javax.annotation.Nullable
  public List<TimeWindow> getTimeWindows() {
    return timeWindows;
  }

  public void setTimeWindows(List<TimeWindow> timeWindows) {
    this.timeWindows = timeWindows;
  }


  public Service type(TypeEnum type) {
    this.type = type;
    return this;
  }

  /**
   * Specifies type of service. This makes a difference if items are loaded or unloaded, i.e. if one of the size dimensions &gt; 0. If it is specified as &#x60;service&#x60; or &#x60;pickup&#x60;, items are loaded and will stay in the vehicle for the rest of the route (and thus consumes capacity for the rest of the route). If it is a &#x60;delivery&#x60;, items are implicitly loaded at the beginning of the route and will stay in the route until delivery (and thus releases capacity for the rest of the route).
   * @return type
   */
  @javax.annotation.Nullable
  public TypeEnum getType() {
    return type;
  }

  public void setType(TypeEnum type) {
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
    Service service = (Service) o;
    return Objects.equals(this.address, service.address) &&
        Objects.equals(this.allowedVehicles, service.allowedVehicles) &&
        Objects.equals(this.disallowedVehicles, service.disallowedVehicles) &&
        Objects.equals(this.duration, service.duration) &&
        Objects.equals(this.group, service.group) &&
        Objects.equals(this.id, service.id) &&
        Objects.equals(this.maxTimeInVehicle, service.maxTimeInVehicle) &&
        Objects.equals(this.name, service.name) &&
        Objects.equals(this.preparationTime, service.preparationTime) &&
        Objects.equals(this.priority, service.priority) &&
        Objects.equals(this.requiredSkills, service.requiredSkills) &&
        Objects.equals(this.size, service.size) &&
        Objects.equals(this.timeWindows, service.timeWindows) &&
        Objects.equals(this.type, service.type);
  }

  @Override
  public int hashCode() {
    return Objects.hash(address, allowedVehicles, disallowedVehicles, duration, group, id, maxTimeInVehicle, name, preparationTime, priority, requiredSkills, size, timeWindows, type);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Service {\n");
    sb.append("    address: ").append(toIndentedString(address)).append("\n");
    sb.append("    allowedVehicles: ").append(toIndentedString(allowedVehicles)).append("\n");
    sb.append("    disallowedVehicles: ").append(toIndentedString(disallowedVehicles)).append("\n");
    sb.append("    duration: ").append(toIndentedString(duration)).append("\n");
    sb.append("    group: ").append(toIndentedString(group)).append("\n");
    sb.append("    id: ").append(toIndentedString(id)).append("\n");
    sb.append("    maxTimeInVehicle: ").append(toIndentedString(maxTimeInVehicle)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    preparationTime: ").append(toIndentedString(preparationTime)).append("\n");
    sb.append("    priority: ").append(toIndentedString(priority)).append("\n");
    sb.append("    requiredSkills: ").append(toIndentedString(requiredSkills)).append("\n");
    sb.append("    size: ").append(toIndentedString(size)).append("\n");
    sb.append("    timeWindows: ").append(toIndentedString(timeWindows)).append("\n");
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
    openapiFields.add("address");
    openapiFields.add("allowed_vehicles");
    openapiFields.add("disallowed_vehicles");
    openapiFields.add("duration");
    openapiFields.add("group");
    openapiFields.add("id");
    openapiFields.add("max_time_in_vehicle");
    openapiFields.add("name");
    openapiFields.add("preparation_time");
    openapiFields.add("priority");
    openapiFields.add("required_skills");
    openapiFields.add("size");
    openapiFields.add("time_windows");
    openapiFields.add("type");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("id");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to Service
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!Service.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in Service is not found in the empty JSON string", Service.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!Service.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `Service` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : Service.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // validate the optional field `address`
      if (jsonObj.get("address") != null && !jsonObj.get("address").isJsonNull()) {
        Address.validateJsonElement(jsonObj.get("address"));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("allowed_vehicles") != null && !jsonObj.get("allowed_vehicles").isJsonNull() && !jsonObj.get("allowed_vehicles").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `allowed_vehicles` to be an array in the JSON string but got `%s`", jsonObj.get("allowed_vehicles").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("disallowed_vehicles") != null && !jsonObj.get("disallowed_vehicles").isJsonNull() && !jsonObj.get("disallowed_vehicles").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `disallowed_vehicles` to be an array in the JSON string but got `%s`", jsonObj.get("disallowed_vehicles").toString()));
      }
      if ((jsonObj.get("group") != null && !jsonObj.get("group").isJsonNull()) && !jsonObj.get("group").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `group` to be a primitive type in the JSON string but got `%s`", jsonObj.get("group").toString()));
      }
      if (!jsonObj.get("id").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `id` to be a primitive type in the JSON string but got `%s`", jsonObj.get("id").toString()));
      }
      if ((jsonObj.get("name") != null && !jsonObj.get("name").isJsonNull()) && !jsonObj.get("name").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `name` to be a primitive type in the JSON string but got `%s`", jsonObj.get("name").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("required_skills") != null && !jsonObj.get("required_skills").isJsonNull() && !jsonObj.get("required_skills").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `required_skills` to be an array in the JSON string but got `%s`", jsonObj.get("required_skills").toString()));
      }
      // ensure the optional json data is an array if present
      if (jsonObj.get("size") != null && !jsonObj.get("size").isJsonNull() && !jsonObj.get("size").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `size` to be an array in the JSON string but got `%s`", jsonObj.get("size").toString()));
      }
      if (jsonObj.get("time_windows") != null && !jsonObj.get("time_windows").isJsonNull()) {
        JsonArray jsonArraytimeWindows = jsonObj.getAsJsonArray("time_windows");
        if (jsonArraytimeWindows != null) {
          // ensure the json data is an array
          if (!jsonObj.get("time_windows").isJsonArray()) {
            throw new IllegalArgumentException(String.format("Expected the field `time_windows` to be an array in the JSON string but got `%s`", jsonObj.get("time_windows").toString()));
          }

          // validate the optional field `time_windows` (array)
          for (int i = 0; i < jsonArraytimeWindows.size(); i++) {
            TimeWindow.validateJsonElement(jsonArraytimeWindows.get(i));
          };
        }
      }
      if ((jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) && !jsonObj.get("type").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `type` to be a primitive type in the JSON string but got `%s`", jsonObj.get("type").toString()));
      }
      // validate the optional field `type`
      if (jsonObj.get("type") != null && !jsonObj.get("type").isJsonNull()) {
        TypeEnum.validateJsonElement(jsonObj.get("type"));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!Service.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'Service' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<Service> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(Service.class));

       return (TypeAdapter<T>) new TypeAdapter<Service>() {
           @Override
           public void write(JsonWriter out, Service value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public Service read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of Service given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of Service
   * @throws IOException if the JSON string is invalid with respect to Service
   */
  public static Service fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, Service.class);
  }

  /**
   * Convert an instance of Service to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

