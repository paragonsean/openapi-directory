/*
 * ConfigCat Public Management API
 * **Base API URL**: https://api.configcat.com  If you prefer the swagger documentation, you can find it here: [Swagger UI](https://api.configcat.com/swagger).  The purpose of this API is to access the ConfigCat platform programmatically.  You can **Create**, **Read**, **Update** and **Delete** any entities like **Feature Flags, Configs, Environments** or **Products** within ConfigCat.   The API is based on HTTP REST, uses resource-oriented URLs, status codes and supports JSON  and JSON+HAL format. Do not use this API for accessing and evaluating feature flag values. Use the [SDKs instead](https://configcat.com/docs/sdk-reference/overview).   # OpenAPI Specification  The complete specification is publicly available here: [swagger.json](v1/swagger.json).  You can use it to generate client libraries in various languages with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) or [Swagger Codegen](https://swagger.io/tools/swagger-codegen/) to interact with this API.  # Authentication This API uses the [Basic HTTP Authentication Scheme](https://en.wikipedia.org/wiki/Basic_access_authentication).   <!-- ReDoc-Inject: <security-definitions> -->  # Throttling and rate limits All the rate limited API calls are returning information about the current rate limit period in the following HTTP headers:  | Header | Description | | :- | :- | | X-Rate-Limit-Remaining | The maximum number of requests remaining in the current rate limit period. | | X-Rate-Limit-Reset     | The time when the current rate limit period resets.        |  When the rate limit is exceeded by a request, the API returns with a `HTTP 429 - Too many requests` status along with a `Retry-After` HTTP header. 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@configcat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.AccessType;
import org.openapitools.client.model.EnvironmentAccessModel;
import org.openapitools.client.model.EnvironmentAccessType;
import org.openapitools.client.model.ProductModel;
import org.openapitools.jackson.nullable.JsonNullable;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for PermissionGroupModel
 */
public class PermissionGroupModelTest {
    private final PermissionGroupModel model = new PermissionGroupModel();

    /**
     * Model tests for PermissionGroupModel
     */
    @Test
    public void testPermissionGroupModel() {
        // TODO: test PermissionGroupModel
    }

    /**
     * Test the property 'accessType'
     */
    @Test
    public void accessTypeTest() {
        // TODO: test accessType
    }

    /**
     * Test the property 'canCreateOrUpdateConfig'
     */
    @Test
    public void canCreateOrUpdateConfigTest() {
        // TODO: test canCreateOrUpdateConfig
    }

    /**
     * Test the property 'canCreateOrUpdateEnvironment'
     */
    @Test
    public void canCreateOrUpdateEnvironmentTest() {
        // TODO: test canCreateOrUpdateEnvironment
    }

    /**
     * Test the property 'canCreateOrUpdateSegments'
     */
    @Test
    public void canCreateOrUpdateSegmentsTest() {
        // TODO: test canCreateOrUpdateSegments
    }

    /**
     * Test the property 'canCreateOrUpdateSetting'
     */
    @Test
    public void canCreateOrUpdateSettingTest() {
        // TODO: test canCreateOrUpdateSetting
    }

    /**
     * Test the property 'canCreateOrUpdateTag'
     */
    @Test
    public void canCreateOrUpdateTagTest() {
        // TODO: test canCreateOrUpdateTag
    }

    /**
     * Test the property 'canDeleteConfig'
     */
    @Test
    public void canDeleteConfigTest() {
        // TODO: test canDeleteConfig
    }

    /**
     * Test the property 'canDeleteEnvironment'
     */
    @Test
    public void canDeleteEnvironmentTest() {
        // TODO: test canDeleteEnvironment
    }

    /**
     * Test the property 'canDeleteSegments'
     */
    @Test
    public void canDeleteSegmentsTest() {
        // TODO: test canDeleteSegments
    }

    /**
     * Test the property 'canDeleteSetting'
     */
    @Test
    public void canDeleteSettingTest() {
        // TODO: test canDeleteSetting
    }

    /**
     * Test the property 'canDeleteTag'
     */
    @Test
    public void canDeleteTagTest() {
        // TODO: test canDeleteTag
    }

    /**
     * Test the property 'canManageIntegrations'
     */
    @Test
    public void canManageIntegrationsTest() {
        // TODO: test canManageIntegrations
    }

    /**
     * Test the property 'canManageMembers'
     */
    @Test
    public void canManageMembersTest() {
        // TODO: test canManageMembers
    }

    /**
     * Test the property 'canManageProductPreferences'
     */
    @Test
    public void canManageProductPreferencesTest() {
        // TODO: test canManageProductPreferences
    }

    /**
     * Test the property 'canManageWebhook'
     */
    @Test
    public void canManageWebhookTest() {
        // TODO: test canManageWebhook
    }

    /**
     * Test the property 'canRotateSdkKey'
     */
    @Test
    public void canRotateSdkKeyTest() {
        // TODO: test canRotateSdkKey
    }

    /**
     * Test the property 'canTagSetting'
     */
    @Test
    public void canTagSettingTest() {
        // TODO: test canTagSetting
    }

    /**
     * Test the property 'canUseExportImport'
     */
    @Test
    public void canUseExportImportTest() {
        // TODO: test canUseExportImport
    }

    /**
     * Test the property 'canViewProductAuditLog'
     */
    @Test
    public void canViewProductAuditLogTest() {
        // TODO: test canViewProductAuditLog
    }

    /**
     * Test the property 'canViewProductStatistics'
     */
    @Test
    public void canViewProductStatisticsTest() {
        // TODO: test canViewProductStatistics
    }

    /**
     * Test the property 'canViewSdkKey'
     */
    @Test
    public void canViewSdkKeyTest() {
        // TODO: test canViewSdkKey
    }

    /**
     * Test the property 'environmentAccesses'
     */
    @Test
    public void environmentAccessesTest() {
        // TODO: test environmentAccesses
    }

    /**
     * Test the property 'name'
     */
    @Test
    public void nameTest() {
        // TODO: test name
    }

    /**
     * Test the property 'newEnvironmentAccessType'
     */
    @Test
    public void newEnvironmentAccessTypeTest() {
        // TODO: test newEnvironmentAccessType
    }

    /**
     * Test the property 'permissionGroupId'
     */
    @Test
    public void permissionGroupIdTest() {
        // TODO: test permissionGroupId
    }

    /**
     * Test the property 'product'
     */
    @Test
    public void productTest() {
        // TODO: test product
    }

}
