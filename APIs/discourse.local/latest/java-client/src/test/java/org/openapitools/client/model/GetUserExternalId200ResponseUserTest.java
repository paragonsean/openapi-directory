/*
 * Discourse API Documentation
 * This page contains the documentation on how to use Discourse through API calls.  > Note: For any endpoints not listed you can follow the [reverse engineer the Discourse API](https://meta.discourse.org/t/-/20576) guide to figure out how to use an API endpoint.  ### Request Content-Type  The Content-Type for POST and PUT requests can be set to `application/x-www-form-urlencoded`, `multipart/form-data`, or `application/json`.  ### Endpoint Names and Response Content-Type  Most API endpoints provide the same content as their HTML counterparts. For example the URL `/categories` serves a list of categories, the `/categories.json` API provides the same information in JSON format.  Instead of sending API requests to `/categories.json` you may also send them to `/categories` and add an `Accept: application/json` header to the request to get the JSON response. Sending requests with the `Accept` header is necessary if you want to use URLs for related endpoints returned by the API, such as pagination URLs. These URLs are returned without the `.json` prefix so you need to add the header in order to get the correct response format.  ### Authentication  Some endpoints do not require any authentication, pretty much anything else will require you to be authenticated.  To become authenticated you will need to create an API Key from the admin panel.  Once you have your API Key you can pass it in along with your API Username as an HTTP header like this:  ``` curl -X GET \"http://127.0.0.1:3000/admin/users/list/active.json\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" ```  and this is how POST requests will look:  ``` curl -X POST \"http://127.0.0.1:3000/categories\" \\ -H \"Content-Type: multipart/form-data;\" \\ -H \"Api-Key: 714552c6148e1617aeab526d0606184b94a80ec048fc09894ff1a72b740c5f19\" \\ -H \"Api-Username: system\" \\ -F \"name=89853c20-4409-e91a-a8ea-f6cdff96aaaa\" \\ -F \"color=49d9e9\" \\ -F \"text_color=f0fcfd\" ```  ### Boolean values  If an endpoint accepts a boolean be sure to specify it as a lowercase `true` or `false` value unless noted otherwise. 
 *
 * The version of the OpenAPI document: latest
 * 
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
import org.openapitools.client.model.AdminGetUser200ResponseGroupsInner;
import org.openapitools.client.model.GetUserExternalId200ResponseUserCustomFields;
import org.openapitools.client.model.GetUserExternalId200ResponseUserGroupUsersInner;
import org.openapitools.client.model.GetUserExternalId200ResponseUserUserAuthTokensInner;
import org.openapitools.client.model.GetUserExternalId200ResponseUserUserFields;
import org.openapitools.client.model.GetUserExternalId200ResponseUserUserNotificationSchedule;
import org.openapitools.client.model.GetUserExternalId200ResponseUserUserOption;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for GetUserExternalId200ResponseUser
 */
public class GetUserExternalId200ResponseUserTest {
    private final GetUserExternalId200ResponseUser model = new GetUserExternalId200ResponseUser();

    /**
     * Model tests for GetUserExternalId200ResponseUser
     */
    @Test
    public void testGetUserExternalId200ResponseUser() {
        // TODO: test GetUserExternalId200ResponseUser
    }

    /**
     * Test the property 'admin'
     */
    @Test
    public void adminTest() {
        // TODO: test admin
    }

    /**
     * Test the property 'allowedPmUsernames'
     */
    @Test
    public void allowedPmUsernamesTest() {
        // TODO: test allowedPmUsernames
    }

    /**
     * Test the property 'avatarTemplate'
     */
    @Test
    public void avatarTemplateTest() {
        // TODO: test avatarTemplate
    }

    /**
     * Test the property 'badgeCount'
     */
    @Test
    public void badgeCountTest() {
        // TODO: test badgeCount
    }

    /**
     * Test the property 'canBeDeleted'
     */
    @Test
    public void canBeDeletedTest() {
        // TODO: test canBeDeleted
    }

    /**
     * Test the property 'canChangeBio'
     */
    @Test
    public void canChangeBioTest() {
        // TODO: test canChangeBio
    }

    /**
     * Test the property 'canChangeLocation'
     */
    @Test
    public void canChangeLocationTest() {
        // TODO: test canChangeLocation
    }

    /**
     * Test the property 'canChangeTrackingPreferences'
     */
    @Test
    public void canChangeTrackingPreferencesTest() {
        // TODO: test canChangeTrackingPreferences
    }

    /**
     * Test the property 'canChangeWebsite'
     */
    @Test
    public void canChangeWebsiteTest() {
        // TODO: test canChangeWebsite
    }

    /**
     * Test the property 'canDeleteAllPosts'
     */
    @Test
    public void canDeleteAllPostsTest() {
        // TODO: test canDeleteAllPosts
    }

    /**
     * Test the property 'canEdit'
     */
    @Test
    public void canEditTest() {
        // TODO: test canEdit
    }

    /**
     * Test the property 'canEditEmail'
     */
    @Test
    public void canEditEmailTest() {
        // TODO: test canEditEmail
    }

    /**
     * Test the property 'canEditName'
     */
    @Test
    public void canEditNameTest() {
        // TODO: test canEditName
    }

    /**
     * Test the property 'canEditUsername'
     */
    @Test
    public void canEditUsernameTest() {
        // TODO: test canEditUsername
    }

    /**
     * Test the property 'canIgnoreUser'
     */
    @Test
    public void canIgnoreUserTest() {
        // TODO: test canIgnoreUser
    }

    /**
     * Test the property 'canMuteUser'
     */
    @Test
    public void canMuteUserTest() {
        // TODO: test canMuteUser
    }

    /**
     * Test the property 'canSendPrivateMessageToUser'
     */
    @Test
    public void canSendPrivateMessageToUserTest() {
        // TODO: test canSendPrivateMessageToUser
    }

    /**
     * Test the property 'canSendPrivateMessages'
     */
    @Test
    public void canSendPrivateMessagesTest() {
        // TODO: test canSendPrivateMessages
    }

    /**
     * Test the property 'canUploadProfileHeader'
     */
    @Test
    public void canUploadProfileHeaderTest() {
        // TODO: test canUploadProfileHeader
    }

    /**
     * Test the property 'canUploadUserCardBackground'
     */
    @Test
    public void canUploadUserCardBackgroundTest() {
        // TODO: test canUploadUserCardBackground
    }

    /**
     * Test the property 'createdAt'
     */
    @Test
    public void createdAtTest() {
        // TODO: test createdAt
    }

    /**
     * Test the property 'customFields'
     */
    @Test
    public void customFieldsTest() {
        // TODO: test customFields
    }

    /**
     * Test the property 'featuredTopic'
     */
    @Test
    public void featuredTopicTest() {
        // TODO: test featuredTopic
    }

    /**
     * Test the property 'featuredUserBadgeIds'
     */
    @Test
    public void featuredUserBadgeIdsTest() {
        // TODO: test featuredUserBadgeIds
    }

    /**
     * Test the property 'flairBgColor'
     */
    @Test
    public void flairBgColorTest() {
        // TODO: test flairBgColor
    }

    /**
     * Test the property 'flairColor'
     */
    @Test
    public void flairColorTest() {
        // TODO: test flairColor
    }

    /**
     * Test the property 'flairGroupId'
     */
    @Test
    public void flairGroupIdTest() {
        // TODO: test flairGroupId
    }

    /**
     * Test the property 'flairName'
     */
    @Test
    public void flairNameTest() {
        // TODO: test flairName
    }

    /**
     * Test the property 'flairUrl'
     */
    @Test
    public void flairUrlTest() {
        // TODO: test flairUrl
    }

    /**
     * Test the property 'groupUsers'
     */
    @Test
    public void groupUsersTest() {
        // TODO: test groupUsers
    }

    /**
     * Test the property 'groups'
     */
    @Test
    public void groupsTest() {
        // TODO: test groups
    }

    /**
     * Test the property 'hasTitleBadges'
     */
    @Test
    public void hasTitleBadgesTest() {
        // TODO: test hasTitleBadges
    }

    /**
     * Test the property 'id'
     */
    @Test
    public void idTest() {
        // TODO: test id
    }

    /**
     * Test the property 'ignored'
     */
    @Test
    public void ignoredTest() {
        // TODO: test ignored
    }

    /**
     * Test the property 'ignoredUsernames'
     */
    @Test
    public void ignoredUsernamesTest() {
        // TODO: test ignoredUsernames
    }

    /**
     * Test the property 'invitedBy'
     */
    @Test
    public void invitedByTest() {
        // TODO: test invitedBy
    }

    /**
     * Test the property 'lastPostedAt'
     */
    @Test
    public void lastPostedAtTest() {
        // TODO: test lastPostedAt
    }

    /**
     * Test the property 'lastSeenAt'
     */
    @Test
    public void lastSeenAtTest() {
        // TODO: test lastSeenAt
    }

    /**
     * Test the property 'locale'
     */
    @Test
    public void localeTest() {
        // TODO: test locale
    }

    /**
     * Test the property 'mailingListPostsPerDay'
     */
    @Test
    public void mailingListPostsPerDayTest() {
        // TODO: test mailingListPostsPerDay
    }

    /**
     * Test the property 'moderator'
     */
    @Test
    public void moderatorTest() {
        // TODO: test moderator
    }

    /**
     * Test the property 'muted'
     */
    @Test
    public void mutedTest() {
        // TODO: test muted
    }

    /**
     * Test the property 'mutedCategoryIds'
     */
    @Test
    public void mutedCategoryIdsTest() {
        // TODO: test mutedCategoryIds
    }

    /**
     * Test the property 'mutedTags'
     */
    @Test
    public void mutedTagsTest() {
        // TODO: test mutedTags
    }

    /**
     * Test the property 'mutedUsernames'
     */
    @Test
    public void mutedUsernamesTest() {
        // TODO: test mutedUsernames
    }

    /**
     * Test the property 'name'
     */
    @Test
    public void nameTest() {
        // TODO: test name
    }

    /**
     * Test the property 'pendingCount'
     */
    @Test
    public void pendingCountTest() {
        // TODO: test pendingCount
    }

    /**
     * Test the property 'pendingPostsCount'
     */
    @Test
    public void pendingPostsCountTest() {
        // TODO: test pendingPostsCount
    }

    /**
     * Test the property 'postCount'
     */
    @Test
    public void postCountTest() {
        // TODO: test postCount
    }

    /**
     * Test the property 'primaryGroupId'
     */
    @Test
    public void primaryGroupIdTest() {
        // TODO: test primaryGroupId
    }

    /**
     * Test the property 'primaryGroupName'
     */
    @Test
    public void primaryGroupNameTest() {
        // TODO: test primaryGroupName
    }

    /**
     * Test the property 'profileViewCount'
     */
    @Test
    public void profileViewCountTest() {
        // TODO: test profileViewCount
    }

    /**
     * Test the property 'recentTimeRead'
     */
    @Test
    public void recentTimeReadTest() {
        // TODO: test recentTimeRead
    }

    /**
     * Test the property 'regularCategoryIds'
     */
    @Test
    public void regularCategoryIdsTest() {
        // TODO: test regularCategoryIds
    }

    /**
     * Test the property 'secondFactorBackupEnabled'
     */
    @Test
    public void secondFactorBackupEnabledTest() {
        // TODO: test secondFactorBackupEnabled
    }

    /**
     * Test the property 'secondFactorEnabled'
     */
    @Test
    public void secondFactorEnabledTest() {
        // TODO: test secondFactorEnabled
    }

    /**
     * Test the property 'staged'
     */
    @Test
    public void stagedTest() {
        // TODO: test staged
    }

    /**
     * Test the property 'systemAvatarTemplate'
     */
    @Test
    public void systemAvatarTemplateTest() {
        // TODO: test systemAvatarTemplate
    }

    /**
     * Test the property 'systemAvatarUploadId'
     */
    @Test
    public void systemAvatarUploadIdTest() {
        // TODO: test systemAvatarUploadId
    }

    /**
     * Test the property 'timeRead'
     */
    @Test
    public void timeReadTest() {
        // TODO: test timeRead
    }

    /**
     * Test the property 'title'
     */
    @Test
    public void titleTest() {
        // TODO: test title
    }

    /**
     * Test the property 'trackedCategoryIds'
     */
    @Test
    public void trackedCategoryIdsTest() {
        // TODO: test trackedCategoryIds
    }

    /**
     * Test the property 'trackedTags'
     */
    @Test
    public void trackedTagsTest() {
        // TODO: test trackedTags
    }

    /**
     * Test the property 'trustLevel'
     */
    @Test
    public void trustLevelTest() {
        // TODO: test trustLevel
    }

    /**
     * Test the property 'uploadedAvatarId'
     */
    @Test
    public void uploadedAvatarIdTest() {
        // TODO: test uploadedAvatarId
    }

    /**
     * Test the property 'useLogoSmallAsAvatar'
     */
    @Test
    public void useLogoSmallAsAvatarTest() {
        // TODO: test useLogoSmallAsAvatar
    }

    /**
     * Test the property 'userApiKeys'
     */
    @Test
    public void userApiKeysTest() {
        // TODO: test userApiKeys
    }

    /**
     * Test the property 'userAuthTokens'
     */
    @Test
    public void userAuthTokensTest() {
        // TODO: test userAuthTokens
    }

    /**
     * Test the property 'userFields'
     */
    @Test
    public void userFieldsTest() {
        // TODO: test userFields
    }

    /**
     * Test the property 'userNotificationSchedule'
     */
    @Test
    public void userNotificationScheduleTest() {
        // TODO: test userNotificationSchedule
    }

    /**
     * Test the property 'userOption'
     */
    @Test
    public void userOptionTest() {
        // TODO: test userOption
    }

    /**
     * Test the property 'username'
     */
    @Test
    public void usernameTest() {
        // TODO: test username
    }

    /**
     * Test the property 'watchedCategoryIds'
     */
    @Test
    public void watchedCategoryIdsTest() {
        // TODO: test watchedCategoryIds
    }

    /**
     * Test the property 'watchedFirstPostCategoryIds'
     */
    @Test
    public void watchedFirstPostCategoryIdsTest() {
        // TODO: test watchedFirstPostCategoryIds
    }

    /**
     * Test the property 'watchedTags'
     */
    @Test
    public void watchedTagsTest() {
        // TODO: test watchedTags
    }

    /**
     * Test the property 'watchingFirstPostTags'
     */
    @Test
    public void watchingFirstPostTagsTest() {
        // TODO: test watchingFirstPostTags
    }

}
