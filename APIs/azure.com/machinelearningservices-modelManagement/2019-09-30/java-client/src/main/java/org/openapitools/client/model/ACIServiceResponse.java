/*
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
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
import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.openapitools.client.model.ContainerResourceRequirements;
import org.openapitools.client.model.DockerImageResponse;
import org.openapitools.client.model.Model;
import org.openapitools.client.model.ModelDataCollection;
import org.openapitools.client.model.ModelEnvironmentDefinition;
import org.openapitools.client.model.ModelErrorResponse;
import org.openapitools.client.model.ServiceResponseBase;

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
 * The response for an ACI service.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:35:06.363531-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ACIServiceResponse extends ServiceResponseBase {
  public static final String SERIALIZED_NAME_APP_INSIGHTS_ENABLED = "appInsightsEnabled";
  @SerializedName(SERIALIZED_NAME_APP_INSIGHTS_ENABLED)
  private Boolean appInsightsEnabled;

  public static final String SERIALIZED_NAME_AUTH_ENABLED = "authEnabled";
  @SerializedName(SERIALIZED_NAME_AUTH_ENABLED)
  private Boolean authEnabled;

  public static final String SERIALIZED_NAME_CNAME = "cname";
  @SerializedName(SERIALIZED_NAME_CNAME)
  private String cname;

  public static final String SERIALIZED_NAME_CONTAINER_RESOURCE_REQUIREMENTS = "containerResourceRequirements";
  @SerializedName(SERIALIZED_NAME_CONTAINER_RESOURCE_REQUIREMENTS)
  private ContainerResourceRequirements containerResourceRequirements;

  public static final String SERIALIZED_NAME_DATA_COLLECTION = "dataCollection";
  @SerializedName(SERIALIZED_NAME_DATA_COLLECTION)
  private ModelDataCollection dataCollection;

  public static final String SERIALIZED_NAME_ENVIRONMENT = "environment";
  @SerializedName(SERIALIZED_NAME_ENVIRONMENT)
  private ModelEnvironmentDefinition environment;

  public static final String SERIALIZED_NAME_IMAGE_DETAILS = "imageDetails";
  @SerializedName(SERIALIZED_NAME_IMAGE_DETAILS)
  private DockerImageResponse imageDetails;

  public static final String SERIALIZED_NAME_IMAGE_ID = "imageId";
  @SerializedName(SERIALIZED_NAME_IMAGE_ID)
  private String imageId;

  public static final String SERIALIZED_NAME_LOCATION = "location";
  @SerializedName(SERIALIZED_NAME_LOCATION)
  private String location;

  public static final String SERIALIZED_NAME_MODEL_CONFIG_MAP = "modelConfigMap";
  @SerializedName(SERIALIZED_NAME_MODEL_CONFIG_MAP)
  private Map<String, Object> modelConfigMap = new HashMap<>();

  public static final String SERIALIZED_NAME_MODELS = "models";
  @SerializedName(SERIALIZED_NAME_MODELS)
  private List<Model> models = new ArrayList<>();

  public static final String SERIALIZED_NAME_PUBLIC_FQDN = "publicFqdn";
  @SerializedName(SERIALIZED_NAME_PUBLIC_FQDN)
  private String publicFqdn;

  public static final String SERIALIZED_NAME_PUBLIC_IP = "publicIp";
  @SerializedName(SERIALIZED_NAME_PUBLIC_IP)
  private String publicIp;

  public static final String SERIALIZED_NAME_SCORING_URI = "scoringUri";
  @SerializedName(SERIALIZED_NAME_SCORING_URI)
  private String scoringUri;

  public static final String SERIALIZED_NAME_SSL_CERTIFICATE = "sslCertificate";
  @SerializedName(SERIALIZED_NAME_SSL_CERTIFICATE)
  private String sslCertificate;

  public static final String SERIALIZED_NAME_SSL_ENABLED = "sslEnabled";
  @SerializedName(SERIALIZED_NAME_SSL_ENABLED)
  private Boolean sslEnabled;

  public static final String SERIALIZED_NAME_SSL_KEY = "sslKey";
  @SerializedName(SERIALIZED_NAME_SSL_KEY)
  private String sslKey;

  public static final String SERIALIZED_NAME_SWAGGER_URI = "swaggerUri";
  @SerializedName(SERIALIZED_NAME_SWAGGER_URI)
  private String swaggerUri;

  public ACIServiceResponse() {
    this.computeType = this.getClass().getSimpleName();
  }

  public ACIServiceResponse appInsightsEnabled(Boolean appInsightsEnabled) {
    this.appInsightsEnabled = appInsightsEnabled;
    return this;
  }

  /**
   * Whether or not Application Insights is enabled.
   * @return appInsightsEnabled
   */
  @javax.annotation.Nullable
  public Boolean getAppInsightsEnabled() {
    return appInsightsEnabled;
  }

  public void setAppInsightsEnabled(Boolean appInsightsEnabled) {
    this.appInsightsEnabled = appInsightsEnabled;
  }


  public ACIServiceResponse authEnabled(Boolean authEnabled) {
    this.authEnabled = authEnabled;
    return this;
  }

  /**
   * Whether or not authentication is enabled on the service.
   * @return authEnabled
   */
  @javax.annotation.Nullable
  public Boolean getAuthEnabled() {
    return authEnabled;
  }

  public void setAuthEnabled(Boolean authEnabled) {
    this.authEnabled = authEnabled;
  }


  public ACIServiceResponse cname(String cname) {
    this.cname = cname;
    return this;
  }

  /**
   * The CName for the service.
   * @return cname
   */
  @javax.annotation.Nullable
  public String getCname() {
    return cname;
  }

  public void setCname(String cname) {
    this.cname = cname;
  }


  public ACIServiceResponse containerResourceRequirements(ContainerResourceRequirements containerResourceRequirements) {
    this.containerResourceRequirements = containerResourceRequirements;
    return this;
  }

  /**
   * Get containerResourceRequirements
   * @return containerResourceRequirements
   */
  @javax.annotation.Nullable
  public ContainerResourceRequirements getContainerResourceRequirements() {
    return containerResourceRequirements;
  }

  public void setContainerResourceRequirements(ContainerResourceRequirements containerResourceRequirements) {
    this.containerResourceRequirements = containerResourceRequirements;
  }


  public ACIServiceResponse dataCollection(ModelDataCollection dataCollection) {
    this.dataCollection = dataCollection;
    return this;
  }

  /**
   * Get dataCollection
   * @return dataCollection
   */
  @javax.annotation.Nullable
  public ModelDataCollection getDataCollection() {
    return dataCollection;
  }

  public void setDataCollection(ModelDataCollection dataCollection) {
    this.dataCollection = dataCollection;
  }


  public ACIServiceResponse environment(ModelEnvironmentDefinition environment) {
    this.environment = environment;
    return this;
  }

  /**
   * Get environment
   * @return environment
   */
  @javax.annotation.Nullable
  public ModelEnvironmentDefinition getEnvironment() {
    return environment;
  }

  public void setEnvironment(ModelEnvironmentDefinition environment) {
    this.environment = environment;
  }


  public ACIServiceResponse imageDetails(DockerImageResponse imageDetails) {
    this.imageDetails = imageDetails;
    return this;
  }

  /**
   * Get imageDetails
   * @return imageDetails
   */
  @javax.annotation.Nullable
  public DockerImageResponse getImageDetails() {
    return imageDetails;
  }

  public void setImageDetails(DockerImageResponse imageDetails) {
    this.imageDetails = imageDetails;
  }


  public ACIServiceResponse imageId(String imageId) {
    this.imageId = imageId;
    return this;
  }

  /**
   * The Id of the Image.
   * @return imageId
   */
  @javax.annotation.Nullable
  public String getImageId() {
    return imageId;
  }

  public void setImageId(String imageId) {
    this.imageId = imageId;
  }


  public ACIServiceResponse location(String location) {
    this.location = location;
    return this;
  }

  /**
   * The location of the service.
   * @return location
   */
  @javax.annotation.Nullable
  public String getLocation() {
    return location;
  }

  public void setLocation(String location) {
    this.location = location;
  }


  public ACIServiceResponse modelConfigMap(Map<String, Object> modelConfigMap) {
    this.modelConfigMap = modelConfigMap;
    return this;
  }

  public ACIServiceResponse putModelConfigMapItem(String key, Object modelConfigMapItem) {
    if (this.modelConfigMap == null) {
      this.modelConfigMap = new HashMap<>();
    }
    this.modelConfigMap.put(key, modelConfigMapItem);
    return this;
  }

  /**
   * Details on the models and configurations.
   * @return modelConfigMap
   */
  @javax.annotation.Nullable
  public Map<String, Object> getModelConfigMap() {
    return modelConfigMap;
  }

  public void setModelConfigMap(Map<String, Object> modelConfigMap) {
    this.modelConfigMap = modelConfigMap;
  }


  public ACIServiceResponse models(List<Model> models) {
    this.models = models;
    return this;
  }

  public ACIServiceResponse addModelsItem(Model modelsItem) {
    if (this.models == null) {
      this.models = new ArrayList<>();
    }
    this.models.add(modelsItem);
    return this;
  }

  /**
   * The list of models.
   * @return models
   */
  @javax.annotation.Nullable
  public List<Model> getModels() {
    return models;
  }

  public void setModels(List<Model> models) {
    this.models = models;
  }


  public ACIServiceResponse publicFqdn(String publicFqdn) {
    this.publicFqdn = publicFqdn;
    return this;
  }

  /**
   * The public Fqdn for the service.
   * @return publicFqdn
   */
  @javax.annotation.Nullable
  public String getPublicFqdn() {
    return publicFqdn;
  }

  public void setPublicFqdn(String publicFqdn) {
    this.publicFqdn = publicFqdn;
  }


  public ACIServiceResponse publicIp(String publicIp) {
    this.publicIp = publicIp;
    return this;
  }

  /**
   * The public IP address for the service.
   * @return publicIp
   */
  @javax.annotation.Nullable
  public String getPublicIp() {
    return publicIp;
  }

  public void setPublicIp(String publicIp) {
    this.publicIp = publicIp;
  }


  public ACIServiceResponse scoringUri(String scoringUri) {
    this.scoringUri = scoringUri;
    return this;
  }

  /**
   * The Uri for sending scoring requests.
   * @return scoringUri
   */
  @javax.annotation.Nullable
  public String getScoringUri() {
    return scoringUri;
  }

  public void setScoringUri(String scoringUri) {
    this.scoringUri = scoringUri;
  }


  public ACIServiceResponse sslCertificate(String sslCertificate) {
    this.sslCertificate = sslCertificate;
    return this;
  }

  /**
   * The SSL certificate to use if SSL is enabled.
   * @return sslCertificate
   */
  @javax.annotation.Nullable
  public String getSslCertificate() {
    return sslCertificate;
  }

  public void setSslCertificate(String sslCertificate) {
    this.sslCertificate = sslCertificate;
  }


  public ACIServiceResponse sslEnabled(Boolean sslEnabled) {
    this.sslEnabled = sslEnabled;
    return this;
  }

  /**
   * Whether or not SSL is enabled.
   * @return sslEnabled
   */
  @javax.annotation.Nullable
  public Boolean getSslEnabled() {
    return sslEnabled;
  }

  public void setSslEnabled(Boolean sslEnabled) {
    this.sslEnabled = sslEnabled;
  }


  public ACIServiceResponse sslKey(String sslKey) {
    this.sslKey = sslKey;
    return this;
  }

  /**
   * The SSL key for the certificate.
   * @return sslKey
   */
  @javax.annotation.Nullable
  public String getSslKey() {
    return sslKey;
  }

  public void setSslKey(String sslKey) {
    this.sslKey = sslKey;
  }


  public ACIServiceResponse swaggerUri(String swaggerUri) {
    this.swaggerUri = swaggerUri;
    return this;
  }

  /**
   * The Uri for sending swagger requests.
   * @return swaggerUri
   */
  @javax.annotation.Nullable
  public String getSwaggerUri() {
    return swaggerUri;
  }

  public void setSwaggerUri(String swaggerUri) {
    this.swaggerUri = swaggerUri;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    ACIServiceResponse acIServiceResponse = (ACIServiceResponse) o;
    return Objects.equals(this.appInsightsEnabled, acIServiceResponse.appInsightsEnabled) &&
        Objects.equals(this.authEnabled, acIServiceResponse.authEnabled) &&
        Objects.equals(this.cname, acIServiceResponse.cname) &&
        Objects.equals(this.containerResourceRequirements, acIServiceResponse.containerResourceRequirements) &&
        Objects.equals(this.dataCollection, acIServiceResponse.dataCollection) &&
        Objects.equals(this.environment, acIServiceResponse.environment) &&
        Objects.equals(this.imageDetails, acIServiceResponse.imageDetails) &&
        Objects.equals(this.imageId, acIServiceResponse.imageId) &&
        Objects.equals(this.location, acIServiceResponse.location) &&
        Objects.equals(this.modelConfigMap, acIServiceResponse.modelConfigMap) &&
        Objects.equals(this.models, acIServiceResponse.models) &&
        Objects.equals(this.publicFqdn, acIServiceResponse.publicFqdn) &&
        Objects.equals(this.publicIp, acIServiceResponse.publicIp) &&
        Objects.equals(this.scoringUri, acIServiceResponse.scoringUri) &&
        Objects.equals(this.sslCertificate, acIServiceResponse.sslCertificate) &&
        Objects.equals(this.sslEnabled, acIServiceResponse.sslEnabled) &&
        Objects.equals(this.sslKey, acIServiceResponse.sslKey) &&
        Objects.equals(this.swaggerUri, acIServiceResponse.swaggerUri) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return Objects.hash(appInsightsEnabled, authEnabled, cname, containerResourceRequirements, dataCollection, environment, imageDetails, imageId, location, modelConfigMap, models, publicFqdn, publicIp, scoringUri, sslCertificate, sslEnabled, sslKey, swaggerUri, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class ACIServiceResponse {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    appInsightsEnabled: ").append(toIndentedString(appInsightsEnabled)).append("\n");
    sb.append("    authEnabled: ").append(toIndentedString(authEnabled)).append("\n");
    sb.append("    cname: ").append(toIndentedString(cname)).append("\n");
    sb.append("    containerResourceRequirements: ").append(toIndentedString(containerResourceRequirements)).append("\n");
    sb.append("    dataCollection: ").append(toIndentedString(dataCollection)).append("\n");
    sb.append("    environment: ").append(toIndentedString(environment)).append("\n");
    sb.append("    imageDetails: ").append(toIndentedString(imageDetails)).append("\n");
    sb.append("    imageId: ").append(toIndentedString(imageId)).append("\n");
    sb.append("    location: ").append(toIndentedString(location)).append("\n");
    sb.append("    modelConfigMap: ").append(toIndentedString(modelConfigMap)).append("\n");
    sb.append("    models: ").append(toIndentedString(models)).append("\n");
    sb.append("    publicFqdn: ").append(toIndentedString(publicFqdn)).append("\n");
    sb.append("    publicIp: ").append(toIndentedString(publicIp)).append("\n");
    sb.append("    scoringUri: ").append(toIndentedString(scoringUri)).append("\n");
    sb.append("    sslCertificate: ").append(toIndentedString(sslCertificate)).append("\n");
    sb.append("    sslEnabled: ").append(toIndentedString(sslEnabled)).append("\n");
    sb.append("    sslKey: ").append(toIndentedString(sslKey)).append("\n");
    sb.append("    swaggerUri: ").append(toIndentedString(swaggerUri)).append("\n");
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
    openapiFields.add("computeType");
    openapiFields.add("createdTime");
    openapiFields.add("deploymentType");
    openapiFields.add("description");
    openapiFields.add("error");
    openapiFields.add("id");
    openapiFields.add("kvTags");
    openapiFields.add("name");
    openapiFields.add("operationId");
    openapiFields.add("properties");
    openapiFields.add("state");
    openapiFields.add("updatedTime");
    openapiFields.add("appInsightsEnabled");
    openapiFields.add("authEnabled");
    openapiFields.add("cname");
    openapiFields.add("containerResourceRequirements");
    openapiFields.add("dataCollection");
    openapiFields.add("environment");
    openapiFields.add("imageDetails");
    openapiFields.add("imageId");
    openapiFields.add("location");
    openapiFields.add("modelConfigMap");
    openapiFields.add("models");
    openapiFields.add("publicFqdn");
    openapiFields.add("publicIp");
    openapiFields.add("scoringUri");
    openapiFields.add("sslCertificate");
    openapiFields.add("sslEnabled");
    openapiFields.add("sslKey");
    openapiFields.add("swaggerUri");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
    openapiRequiredFields.add("computeType");
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to ACIServiceResponse
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!ACIServiceResponse.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in ACIServiceResponse is not found in the empty JSON string", ACIServiceResponse.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!ACIServiceResponse.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `ACIServiceResponse` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }

      // check to make sure all required properties/fields are present in the JSON string
      for (String requiredField : ACIServiceResponse.openapiRequiredFields) {
        if (jsonElement.getAsJsonObject().get(requiredField) == null) {
          throw new IllegalArgumentException(String.format("The required field `%s` is not found in the JSON string: %s", requiredField, jsonElement.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!ACIServiceResponse.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'ACIServiceResponse' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<ACIServiceResponse> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(ACIServiceResponse.class));

       return (TypeAdapter<T>) new TypeAdapter<ACIServiceResponse>() {
           @Override
           public void write(JsonWriter out, ACIServiceResponse value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public ACIServiceResponse read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of ACIServiceResponse given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of ACIServiceResponse
   * @throws IOException if the JSON string is invalid with respect to ACIServiceResponse
   */
  public static ACIServiceResponse fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, ACIServiceResponse.class);
  }

  /**
   * Convert an instance of ACIServiceResponse to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

