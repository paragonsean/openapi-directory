/*
 * Interactive documentation for your Premium plan
 *   This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the `GET` button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the `Parameters` section and hit `Execute` to view a full API response. You can then inspect the JSON response, copy the `curl` command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
 *
 * The version of the OpenAPI document: v1
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:01:13.236583-04:00[America/New_York]", comments = "Generator version: 7.9.0")
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
