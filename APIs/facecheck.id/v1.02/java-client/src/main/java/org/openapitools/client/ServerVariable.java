/*
 * Facial Recognition Reverse Image Face Search API
 * Let your users search the Internet by face! Integrate FaceCheck facial search seamlessly with your app, website or software platform.   FaceCheck's REST API is hassle-free and easy to use. For code examples visit <a href='https://facecheck.id/Face-Search/API'>https://facecheck.id/Face-Search/API</a>
 *
 * The version of the OpenAPI document: v1.02
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client;

import java.util.HashSet;

/**
 * Representing a Server Variable for server URL template substitution.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:05:45.467249-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServerVariable {
    public String description;
    public String defaultValue;
    public HashSet<String> enumValues = null;

    /**
     * @param description A description for the server variable.
     * @param defaultValue The default value to use for substitution.
     * @param enumValues An enumeration of string values to be used if the substitution options are from a limited set.
     */
    public ServerVariable(String description, String defaultValue, HashSet<String> enumValues) {
        this.description = description;
        this.defaultValue = defaultValue;
        this.enumValues = enumValues;
    }
}
