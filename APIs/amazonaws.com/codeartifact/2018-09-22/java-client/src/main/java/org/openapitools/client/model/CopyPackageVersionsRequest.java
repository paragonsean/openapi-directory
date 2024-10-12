/*
 * CodeArtifact
 * <p> CodeArtifact is a fully managed artifact repository compatible with language-native package managers and build tools such as npm, Apache Maven, pip, and dotnet. You can use CodeArtifact to share packages with development teams and pull packages. Packages can be pulled from both public and CodeArtifact repositories. You can also create an upstream relationship between a CodeArtifact repository and another repository, which effectively merges their contents from the point of view of a package manager client. </p> <p> <b>CodeArtifact Components</b> </p> <p>Use the information in this guide to help you work with the following CodeArtifact components:</p> <ul> <li> <p> <b>Repository</b>: A CodeArtifact repository contains a set of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html#welcome-concepts-package-version\">package versions</a>, each of which maps to a set of assets, or files. Repositories are polyglot, so a single repository can contain packages of any supported type. Each repository exposes endpoints for fetching and publishing packages using tools like the <b> <code>npm</code> </b> CLI, the Maven CLI (<b> <code>mvn</code> </b>), Python CLIs (<b> <code>pip</code> </b> and <code>twine</code>), and NuGet CLIs (<code>nuget</code> and <code>dotnet</code>).</p> </li> <li> <p> <b>Domain</b>: Repositories are aggregated into a higher-level entity known as a <i>domain</i>. All package assets and metadata are stored in the domain, but are consumed through repositories. A given package asset, such as a Maven JAR file, is stored once per domain, no matter how many repositories it's present in. All of the assets and metadata in a domain are encrypted with the same customer master key (CMK) stored in Key Management Service (KMS).</p> <p>Each repository is a member of a single domain and can't be moved to a different domain.</p> <p>The domain allows organizational policy to be applied across multiple repositories, such as which accounts can access repositories in the domain, and which public repositories can be used as sources of packages.</p> <p>Although an organization can have multiple domains, we recommend a single production domain that contains all published artifacts so that teams can find and share packages across their organization.</p> </li> <li> <p> <b>Package</b>: A <i>package</i> is a bundle of software and the metadata required to resolve dependencies and install the software. CodeArtifact supports <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-npm.html\">npm</a>, <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html\">PyPI</a>, <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-maven\">Maven</a>, and <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-nuget\">NuGet</a> package formats.</p> <p>In CodeArtifact, a package consists of:</p> <ul> <li> <p>A <i>name</i> (for example, <code>webpack</code> is the name of a popular npm package)</p> </li> <li> <p>An optional namespace (for example, <code>@types</code> in <code>@types/node</code>)</p> </li> <li> <p>A set of versions (for example, <code>1.0.0</code>, <code>1.0.1</code>, <code>1.0.2</code>, etc.)</p> </li> <li> <p> Package-level metadata (for example, npm tags)</p> </li> </ul> </li> <li> <p> <b>Package version</b>: A version of a package, such as <code>@types/node 12.6.9</code>. The version number format and semantics vary for different package formats. For example, npm package versions must conform to the <a href=\"https://semver.org/\">Semantic Versioning specification</a>. In CodeArtifact, a package version consists of the version identifier, metadata at the package version level, and a set of assets.</p> </li> <li> <p> <b>Upstream repository</b>: One repository is <i>upstream</i> of another when the package versions in it can be accessed from the repository endpoint of the downstream repository, effectively merging the contents of the two repositories from the point of view of a client. CodeArtifact allows creating an upstream relationship between two repositories.</p> </li> <li> <p> <b>Asset</b>: An individual file stored in CodeArtifact associated with a package version, such as an npm <code>.tgz</code> file or Maven POM and JAR files.</p> </li> </ul> <p>CodeArtifact supports these operations:</p> <ul> <li> <p> <code>AssociateExternalConnection</code>: Adds an existing external connection to a repository. </p> </li> <li> <p> <code>CopyPackageVersions</code>: Copies package versions from one repository to another repository in the same domain.</p> </li> <li> <p> <code>CreateDomain</code>: Creates a domain</p> </li> <li> <p> <code>CreateRepository</code>: Creates a CodeArtifact repository in a domain. </p> </li> <li> <p> <code>DeleteDomain</code>: Deletes a domain. You cannot delete a domain that contains repositories. </p> </li> <li> <p> <code>DeleteDomainPermissionsPolicy</code>: Deletes the resource policy that is set on a domain.</p> </li> <li> <p> <code>DeletePackage</code>: Deletes a package and all associated package versions.</p> </li> <li> <p> <code>DeletePackageVersions</code>: Deletes versions of a package. After a package has been deleted, it can be republished, but its assets and metadata cannot be restored because they have been permanently removed from storage.</p> </li> <li> <p> <code>DeleteRepository</code>: Deletes a repository. </p> </li> <li> <p> <code>DeleteRepositoryPermissionsPolicy</code>: Deletes the resource policy that is set on a repository.</p> </li> <li> <p> <code>DescribeDomain</code>: Returns a <code>DomainDescription</code> object that contains information about the requested domain.</p> </li> <li> <p> <code>DescribePackage</code>: Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\">PackageDescription</a> object that contains details about a package. </p> </li> <li> <p> <code>DescribePackageVersion</code>: Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\">PackageVersionDescription</a> object that contains details about a package version. </p> </li> <li> <p> <code>DescribeRepository</code>: Returns a <code>RepositoryDescription</code> object that contains detailed information about the requested repository. </p> </li> <li> <p> <code>DisposePackageVersions</code>: Disposes versions of a package. A package version with the status <code>Disposed</code> cannot be restored because they have been permanently removed from storage.</p> </li> <li> <p> <code>DisassociateExternalConnection</code>: Removes an existing external connection from a repository. </p> </li> <li> <p> <code>GetAuthorizationToken</code>: Generates a temporary authorization token for accessing repositories in the domain. The token expires the authorization period has passed. The default authorization period is 12 hours and can be customized to any length with a maximum of 12 hours.</p> </li> <li> <p> <code>GetDomainPermissionsPolicy</code>: Returns the policy of a resource that is attached to the specified domain. </p> </li> <li> <p> <code>GetPackageVersionAsset</code>: Returns the contents of an asset that is in a package version. </p> </li> <li> <p> <code>GetPackageVersionReadme</code>: Gets the readme file or descriptive text for a package version.</p> </li> <li> <p> <code>GetRepositoryEndpoint</code>: Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: </p> <ul> <li> <p> <code>maven</code> </p> </li> <li> <p> <code>npm</code> </p> </li> <li> <p> <code>nuget</code> </p> </li> <li> <p> <code>pypi</code> </p> </li> </ul> </li> <li> <p> <code>GetRepositoryPermissionsPolicy</code>: Returns the resource policy that is set on a repository. </p> </li> <li> <p> <code>ListDomains</code>: Returns a list of <code>DomainSummary</code> objects. Each returned <code>DomainSummary</code> object contains information about a domain.</p> </li> <li> <p> <code>ListPackages</code>: Lists the packages in a repository.</p> </li> <li> <p> <code>ListPackageVersionAssets</code>: Lists the assets for a given package version.</p> </li> <li> <p> <code>ListPackageVersionDependencies</code>: Returns a list of the direct dependencies for a package version. </p> </li> <li> <p> <code>ListPackageVersions</code>: Returns a list of package versions for a specified package in a repository.</p> </li> <li> <p> <code>ListRepositories</code>: Returns a list of repositories owned by the Amazon Web Services account that called this method.</p> </li> <li> <p> <code>ListRepositoriesInDomain</code>: Returns a list of the repositories in a domain.</p> </li> <li> <p> <code>PublishPackageVersion</code>: Creates a new package version containing one or more assets.</p> </li> <li> <p> <code>PutDomainPermissionsPolicy</code>: Attaches a resource policy to a domain.</p> </li> <li> <p> <code>PutPackageOriginConfiguration</code>: Sets the package origin configuration for a package, which determine how new versions of the package can be added to a specific repository.</p> </li> <li> <p> <code>PutRepositoryPermissionsPolicy</code>: Sets the resource policy on a repository that specifies permissions to access it. </p> </li> <li> <p> <code>UpdatePackageVersionsStatus</code>: Updates the status of one or more versions of a package.</p> </li> <li> <p> <code>UpdateRepository</code>: Updates the properties of a repository.</p> </li> </ul>
 *
 * The version of the OpenAPI document: 2018-09-22
 * Contact: mike.ralphson@gmail.com
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
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
 * CopyPackageVersionsRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T12:07:53.978156-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class CopyPackageVersionsRequest {
  public static final String SERIALIZED_NAME_VERSIONS = "versions";
  @SerializedName(SERIALIZED_NAME_VERSIONS)
  private List<String> versions = new ArrayList<>();

  public static final String SERIALIZED_NAME_VERSION_REVISIONS = "versionRevisions";
  @SerializedName(SERIALIZED_NAME_VERSION_REVISIONS)
  private Map<String, String> versionRevisions = new HashMap<>();

  public static final String SERIALIZED_NAME_ALLOW_OVERWRITE = "allowOverwrite";
  @SerializedName(SERIALIZED_NAME_ALLOW_OVERWRITE)
  private Boolean allowOverwrite;

  public static final String SERIALIZED_NAME_INCLUDE_FROM_UPSTREAM = "includeFromUpstream";
  @SerializedName(SERIALIZED_NAME_INCLUDE_FROM_UPSTREAM)
  private Boolean includeFromUpstream;

  public CopyPackageVersionsRequest() {
  }

  public CopyPackageVersionsRequest versions(List<String> versions) {
    this.versions = versions;
    return this;
  }

  public CopyPackageVersionsRequest addVersionsItem(String versionsItem) {
    if (this.versions == null) {
      this.versions = new ArrayList<>();
    }
    this.versions.add(versionsItem);
    return this;
  }

  /**
   * &lt;p&gt; The versions of the package to be copied. &lt;/p&gt; &lt;note&gt; &lt;p&gt; You must specify &lt;code&gt;versions&lt;/code&gt; or &lt;code&gt;versionRevisions&lt;/code&gt;. You cannot specify both. &lt;/p&gt; &lt;/note&gt;
   * @return versions
   */
  @javax.annotation.Nullable
  public List<String> getVersions() {
    return versions;
  }

  public void setVersions(List<String> versions) {
    this.versions = versions;
  }


  public CopyPackageVersionsRequest versionRevisions(Map<String, String> versionRevisions) {
    this.versionRevisions = versionRevisions;
    return this;
  }

  public CopyPackageVersionsRequest putVersionRevisionsItem(String key, String versionRevisionsItem) {
    if (this.versionRevisions == null) {
      this.versionRevisions = new HashMap<>();
    }
    this.versionRevisions.put(key, versionRevisionsItem);
    return this;
  }

  /**
   * &lt;p&gt; A list of key-value pairs. The keys are package versions and the values are package version revisions. A &lt;code&gt;CopyPackageVersion&lt;/code&gt; operation succeeds if the specified versions in the source repository match the specified package version revision. &lt;/p&gt; &lt;note&gt; &lt;p&gt; You must specify &lt;code&gt;versions&lt;/code&gt; or &lt;code&gt;versionRevisions&lt;/code&gt;. You cannot specify both. &lt;/p&gt; &lt;/note&gt;
   * @return versionRevisions
   */
  @javax.annotation.Nullable
  public Map<String, String> getVersionRevisions() {
    return versionRevisions;
  }

  public void setVersionRevisions(Map<String, String> versionRevisions) {
    this.versionRevisions = versionRevisions;
  }


  public CopyPackageVersionsRequest allowOverwrite(Boolean allowOverwrite) {
    this.allowOverwrite = allowOverwrite;
    return this;
  }

  /**
   *  Set to true to overwrite a package version that already exists in the destination repository. If set to false and the package version already exists in the destination repository, the package version is returned in the &lt;code&gt;failedVersions&lt;/code&gt; field of the response with an &lt;code&gt;ALREADY_EXISTS&lt;/code&gt; error code. 
   * @return allowOverwrite
   */
  @javax.annotation.Nullable
  public Boolean getAllowOverwrite() {
    return allowOverwrite;
  }

  public void setAllowOverwrite(Boolean allowOverwrite) {
    this.allowOverwrite = allowOverwrite;
  }


  public CopyPackageVersionsRequest includeFromUpstream(Boolean includeFromUpstream) {
    this.includeFromUpstream = includeFromUpstream;
    return this;
  }

  /**
   *  Set to true to copy packages from repositories that are upstream from the source repository to the destination repository. The default setting is false. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html\&quot;&gt;Working with upstream repositories&lt;/a&gt;. 
   * @return includeFromUpstream
   */
  @javax.annotation.Nullable
  public Boolean getIncludeFromUpstream() {
    return includeFromUpstream;
  }

  public void setIncludeFromUpstream(Boolean includeFromUpstream) {
    this.includeFromUpstream = includeFromUpstream;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CopyPackageVersionsRequest copyPackageVersionsRequest = (CopyPackageVersionsRequest) o;
    return Objects.equals(this.versions, copyPackageVersionsRequest.versions) &&
        Objects.equals(this.versionRevisions, copyPackageVersionsRequest.versionRevisions) &&
        Objects.equals(this.allowOverwrite, copyPackageVersionsRequest.allowOverwrite) &&
        Objects.equals(this.includeFromUpstream, copyPackageVersionsRequest.includeFromUpstream);
  }

  @Override
  public int hashCode() {
    return Objects.hash(versions, versionRevisions, allowOverwrite, includeFromUpstream);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CopyPackageVersionsRequest {\n");
    sb.append("    versions: ").append(toIndentedString(versions)).append("\n");
    sb.append("    versionRevisions: ").append(toIndentedString(versionRevisions)).append("\n");
    sb.append("    allowOverwrite: ").append(toIndentedString(allowOverwrite)).append("\n");
    sb.append("    includeFromUpstream: ").append(toIndentedString(includeFromUpstream)).append("\n");
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
    openapiFields.add("versions");
    openapiFields.add("versionRevisions");
    openapiFields.add("allowOverwrite");
    openapiFields.add("includeFromUpstream");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

  /**
   * Validates the JSON Element and throws an exception if issues found
   *
   * @param jsonElement JSON Element
   * @throws IOException if the JSON Element is invalid with respect to CopyPackageVersionsRequest
   */
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {
      if (jsonElement == null) {
        if (!CopyPackageVersionsRequest.openapiRequiredFields.isEmpty()) { // has required fields but JSON element is null
          throw new IllegalArgumentException(String.format("The required field(s) %s in CopyPackageVersionsRequest is not found in the empty JSON string", CopyPackageVersionsRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Map.Entry<String, JsonElement>> entries = jsonElement.getAsJsonObject().entrySet();
      // check to see if the JSON string contains additional fields
      for (Map.Entry<String, JsonElement> entry : entries) {
        if (!CopyPackageVersionsRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `CopyPackageVersionsRequest` properties. JSON: %s", entry.getKey(), jsonElement.toString()));
        }
      }
        JsonObject jsonObj = jsonElement.getAsJsonObject();
      // ensure the optional json data is an array if present
      if (jsonObj.get("versions") != null && !jsonObj.get("versions").isJsonNull() && !jsonObj.get("versions").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `versions` to be an array in the JSON string but got `%s`", jsonObj.get("versions").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!CopyPackageVersionsRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'CopyPackageVersionsRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<CopyPackageVersionsRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(CopyPackageVersionsRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<CopyPackageVersionsRequest>() {
           @Override
           public void write(JsonWriter out, CopyPackageVersionsRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public CopyPackageVersionsRequest read(JsonReader in) throws IOException {
             JsonElement jsonElement = elementAdapter.read(in);
             validateJsonElement(jsonElement);
             return thisAdapter.fromJsonTree(jsonElement);
           }

       }.nullSafe();
    }
  }

  /**
   * Create an instance of CopyPackageVersionsRequest given an JSON string
   *
   * @param jsonString JSON string
   * @return An instance of CopyPackageVersionsRequest
   * @throws IOException if the JSON string is invalid with respect to CopyPackageVersionsRequest
   */
  public static CopyPackageVersionsRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, CopyPackageVersionsRequest.class);
  }

  /**
   * Convert an instance of CopyPackageVersionsRequest to an JSON string
   *
   * @return JSON string
   */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

