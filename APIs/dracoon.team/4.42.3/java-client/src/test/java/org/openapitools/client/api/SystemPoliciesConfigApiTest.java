/*
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ClassificationPoliciesConfig;
import org.openapitools.client.model.ErrorResponse;
import org.openapitools.client.model.GuestUsersPoliciesConfig;
import org.openapitools.client.model.MfaPoliciesConfig;
import org.openapitools.client.model.PasswordPoliciesConfig;
import org.openapitools.client.model.UpdateClassificationPoliciesConfig;
import org.openapitools.client.model.UpdateGuestUsersPoliciesConfig;
import org.openapitools.client.model.UpdateMfaPoliciesConfig;
import org.openapitools.client.model.UpdatePasswordPoliciesConfig;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SystemPoliciesConfigApi
 */
@Disabled
public class SystemPoliciesConfigApiTest {

    private final SystemPoliciesConfigApi api = new SystemPoliciesConfigApi();

    /**
     * Change classification policies
     *
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.30.0&lt;/h3&gt;  ### Description: Change current classification policies: * &#x60;shareClassificationPolicies&#x60;  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Classification policies are changed.  ### Further Information: &#x60;classificationRequiresSharePassword&#x60;: When a node has this classification or higher, it cannot be shared without a password. If the node is an encrypted file this policy has no effect. &#x60;0&#x60; means no password will be enforced.  
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void changeClassificationPoliciesConfigTest() throws ApiException {
        UpdateClassificationPoliciesConfig updateClassificationPoliciesConfig = null;
        String xSdsAuthToken = null;
        ClassificationPoliciesConfig response = api.changeClassificationPoliciesConfig(updateClassificationPoliciesConfig, xSdsAuthToken);
        // TODO: test validations
    }

    /**
     * Change guest user policies
     *
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.40.0&lt;/h3&gt;  ### Description: Change current guest user policies.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Guest user policies are changed.    ### Further Information: None.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void changeGuestUsersPoliciesConfigTest() throws ApiException {
        UpdateGuestUsersPoliciesConfig updateGuestUsersPoliciesConfig = null;
        String xSdsAuthToken = null;
        GuestUsersPoliciesConfig response = api.changeGuestUsersPoliciesConfig(updateGuestUsersPoliciesConfig, xSdsAuthToken);
        // TODO: test validations
    }

    /**
     * Change MFA policies
     *
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description: Change current multi-factor authentication policies.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Multi-factor authentication policies are changed.    ### Further Information: None.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void changeMfaPoliciesConfigTest() throws ApiException {
        UpdateMfaPoliciesConfig updateMfaPoliciesConfig = null;
        String xSdsAuthToken = null;
        MfaPoliciesConfig response = api.changeMfaPoliciesConfig(updateMfaPoliciesConfig, xSdsAuthToken);
        // TODO: test validations
    }

    /**
     * Change password policies
     *
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.14.0&lt;/h3&gt;  ### Description:   Change current password policies for any password types:   * &#x60;login&#x60; * &#x60;shares&#x60; * &#x60;encryption&#x60;  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Password policies get changed.  ### Further Information: None.  ### Available password policies: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Value | Recommended Value | Password Type | | :--- | :--- | :--- | :--- | :--- | | &#x60;mustContainCharacters&#x60; | Characters which a password must contain:&lt;br&gt;&lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60; - at least one alphabetical character (&#x60;uppercase&#x60; **OR** &#x60;lowercase&#x60;)&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;br&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60; - at least one uppercase character&lt;pre&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60; - at least one lowercase character&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60; - at least one numeric character&lt;pre&gt;0 1 2 3 4 5 6 7 8 9&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60; - at least one special character (letters and digits excluded)&lt;pre&gt;! \&quot; # $ % ( ) * + , - . / : ; &#x3D; ? @ [ \\ ] ^ _ { &amp;#124; } ~&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60; - none of the above&lt;/li&gt;&lt;li&gt;&#x60;all&#x60; - combination of &#x60;uppercase&#x60;, &#x60;lowercase&#x60;, &#x60;numeric&#x60; and &#x60;special&#x60;&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60;&lt;/li&gt;&lt;li&gt;&#x60;all&#x60;&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;uppercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60;&lt;/li&gt;&lt;/ul&gt;  | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfCharacteristicsToEnforce&#x60; | Number of characteristics to enforce.&lt;br&gt;e.g. from &#x60;[\&quot;uppercase\&quot;, \&quot;lowercase\&quot;, \&quot;numeric\&quot;, \&quot;special\&quot;]&#x60;&lt;br&gt;all 4 character sets can be enforced; but also only 2 of them | &#x60;Integer between 0 and 4&#x60;&lt;br&gt;&lt;br&gt;default:&lt;ul&gt;&lt;li&gt;&#x60;none&#x60; - &#x60;0&#x60;&lt;/li&gt;&lt;li&gt;&#x60;all&#x60; - &#x60;4&#x60;&lt;/li&gt;&lt;li&gt;otherwise - amount of distinct values&lt;br&gt;cf. &#x60;mustContainCharacters&#x60; matrix&lt;/li&gt;&lt;/ul&gt; | &#x60;3&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;minLength&#x60; | Minimum number of characters a password must contain. | &#x60;Integer between 1 and 1024&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;: &#x60;12&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;: &#x60;12&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;: &#x60;14&#x60;&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectDictionaryWords&#x60; | Determines whether a password must **NOT** contain word(s) from a dictionary.&lt;br&gt;In &#x60;core-service.properties&#x60; a path to directory with dictionary files (&#x60;*.txt&#x60;) can be defined&lt;br&gt;cf. &#x60;policies.passwords.dictionary.directory&#x60;.&lt;br&gt;&lt;br&gt;If this rule gets enabled &#x60;policies.passwords.dictionary.directory&#x60; must be defined and contain dictionary files.&lt;br&gt;Otherwise, the rule will not have any effect on password validation process. | &#x60;true or false&#x60; | &#x60;true&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectUserInfo&#x60; | Determines whether a password must **NOT** contain user info.&lt;br&gt;Affects user&#39;s **first name**, **last name**, **email** and **user name**. | &#x60;true or false&#x60; | &#x60;true&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectKeyboardPatterns&#x60; | Determines whether a password must **NOT** contain keyboard patterns.&lt;br&gt;e.g. &#x60;qwertz&#x60;, &#x60;asdf&#x60; (min. 4 character pattern) | &#x60;true or false&#x60; | &#x60;true&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfArchivedPasswords&#x60; | Number of passwords to archive. | &#x60;Integer between 0 and 10&#x60;&lt;br&gt;Set &#x60;0&#x60; to disable password history. | &#x60;3&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;passwordExpiration.enabled&#x60; | Determines whether password expiration is enabled.&lt;br&gt;Password expiration policy can only be enabled in context with &#x60;enforceLoginPasswordChange&#x60;. | &#x60;true or false&#x60; | &#x60;false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxPasswordAge&#x60; | Maximum allowed password age (in **days**) | &#x60;positive Integer&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;userLockout.enabled&#x60; | Determines whether user lockout is enabled. | &#x60;true or false&#x60; | &#x60;true&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxNumberOfLoginFailures&#x60; | Maximum allowed number of failed login attempts. | &#x60;positive Integer&#x60; | &#x60;5&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;lockoutPeriod&#x60; | Amount of **minutes** a user has to wait to make another login attempt&lt;br&gt;after &#x60;maxNumberOfLoginFailures&#x60; has been exceeded. | &#x60;positive Integer&#x60; | &#x60;10&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;  ### Deprecated password policies: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Value | Recommended Value | Password Type | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;enforceLoginPasswordChange&#x60;&lt;/del&gt; | Determines whether a login password change should be enforced for all users.&lt;br&gt;Only takes effect, if login password policies get stricter.&lt;br&gt;Use &#x60;POST /system/config/policies/passwords/enforce_change&#x60; API to enforce a login password change. | &#x60;true or false&#x60;&lt;br&gt;default: &#x60;false&#x60; |  | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;  ### &#x60;mustContainCharacters&#x60; matrix: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  |  | &#x60;alpha&#x60; | &#x60;uppercase&#x60; | &#x60;lowercase&#x60; | &#x60;numeric&#x60; | &#x60;special&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | | &#x60;alpha&#x60; | &#x60;alpha&#x60; | &#x60;uppercase&#x60; | &#x60;lowercase&#x60; | &#x60;alpha&#x60;&lt;br&gt;&#x60;numeric&#x60; | &#x60;alpha&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | &#x60;uppercase&#x60; | &#x60;uppercase&#x60; | &#x60;uppercase&#x60; | &#x60;uppercase&#x60;&lt;br&gt;&#x60;lowercase&#x60; | &#x60;uppercase&#x60;&lt;br&gt;&#x60;numeric&#x60; | &#x60;uppercase&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | &#x60;lowercase&#x60; | &#x60;lowercase&#x60; | &#x60;uppercase&#x60;&lt;br&gt;&#x60;lowercase&#x60; | &#x60;lowercase&#x60; | &#x60;lowercase&#x60;&lt;br&gt;&#x60;numeric&#x60; | &#x60;lowercase&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | &#x60;numeric&#x60; | &#x60;alpha&#x60;&lt;br&gt;&#x60;numeric&#x60; | &#x60;uppercase&#x60;&lt;br&gt;&#x60;numeric&#x60; | &#x60;lowercase&#x60;&lt;br&gt;&#x60;numeric&#x60; | &#x60;numeric&#x60; | &#x60;numeric&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | &#x60;special&#x60; | &#x60;alpha&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;uppercase&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;lowercase&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;numeric&#x60;&lt;br&gt;&#x60;special&#x60; | &#x60;special&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | &#x60;all&#x60; | &#x60;all&#x60; | &#x60;all&#x60; | &#x60;all&#x60; | &#x60;all&#x60; | &#x60;all&#x60; | &#x60;all&#x60; | &#x60;none&#x60; | | &#x60;none&#x60; | &#x60;none&#x60; | &#x60;none&#x60; |  &#x60;none&#x60; | &#x60;none&#x60; | &#x60;none&#x60; | &#x60;none&#x60; | &#x60;none&#x60; |  &lt;/details&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void changePasswordPoliciesConfigTest() throws ApiException {
        UpdatePasswordPoliciesConfig updatePasswordPoliciesConfig = null;
        String xSdsAuthToken = null;
        PasswordPoliciesConfig response = api.changePasswordPoliciesConfig(updatePasswordPoliciesConfig, xSdsAuthToken);
        // TODO: test validations
    }

    /**
     * Enforce login password change for all users
     *
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.24.0&lt;/h3&gt;  ### Description:   Enforce login password change for all users.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; change global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Login password change is enforced. Every user has to change their login password at next login.  ### Further Information: None.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void enforceLoginPasswordChangeTest() throws ApiException {
        String xSdsAuthToken = null;
        api.enforceLoginPasswordChange(xSdsAuthToken);
        // TODO: test validations
    }

    /**
     * Request classification policies
     *
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.30.0&lt;/h3&gt;  ### Description:   Retrieve a list of classification policies: * &#x60;shareClassificationPolicies&#x60;  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of configured classification policies is returned.  ### Further Information: &#x60;classificationRequiresSharePassword&#x60;: When a node has this classification or higher, it cannot be shared without a password. If the node is an encrypted file this policy has no effect. &#x60;0&#x60; means no password will be enforced. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void requestClassificationPoliciesConfigTest() throws ApiException {
        String xSdsAuthToken = null;
        ClassificationPoliciesConfig response = api.requestClassificationPoliciesConfig(xSdsAuthToken);
        // TODO: test validations
    }

    /**
     * Request guest user policies
     *
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.40.0&lt;/h3&gt;  ### Description:   Retrieve guest user policies.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: Guest user policies are returned.  ### Further Information: None.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void requestGuestUsersPoliciesConfigTest() throws ApiException {
        String xSdsAuthToken = null;
        GuestUsersPoliciesConfig response = api.requestGuestUsersPoliciesConfig(xSdsAuthToken);
        // TODO: test validations
    }

    /**
     * Request MFA policies
     *
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.37.0&lt;/h3&gt;  ### Description:   Retrieve a list of multi-factor authentication policies.    ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of configured multi-factor authentication policies is returned.  ### Further Information: None.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void requestMfaPoliciesConfigTest() throws ApiException {
        String xSdsAuthToken = null;
        MfaPoliciesConfig response = api.requestMfaPoliciesConfig(xSdsAuthToken);
        // TODO: test validations
    }

    /**
     * Request password policies
     *
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.14.0&lt;/h3&gt;  ### Description:   Retrieve a list of configured password policies for all password types:   * &#x60;login&#x60; * &#x60;shares&#x60; * &#x60;encryption&#x60;  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of configured password policies is returned.  ### Further Information: None.  ### Available password policies: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Value | Password Type | | :--- | :--- | :--- | :--- | | &#x60;mustContainCharacters&#x60; | Characters which a password must contain:&lt;br&gt;&lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60; - at least one alphabetical character (&#x60;uppercase&#x60; **OR** &#x60;lowercase&#x60;)&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;br&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60; - at least one uppercase character&lt;pre&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60; - at least one lowercase character&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60; - at least one numeric character&lt;pre&gt;0 1 2 3 4 5 6 7 8 9&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60; - at least one special character (letters and digits excluded)&lt;pre&gt;! \&quot; # $ % ( ) * + , - . / : ; &#x3D; ? @ [ \\ ] ^ _ { &amp;#124; } ~&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60; - none of the above&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60;&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfCharacteristicsToEnforce&#x60; | Number of characteristics to enforce.&lt;br&gt;e.g. from &#x60;[\&quot;uppercase\&quot;, \&quot;lowercase\&quot;, \&quot;numeric\&quot;, \&quot;special\&quot;]&#x60;&lt;br&gt;all 4 character sets can be enforced; but also only 2 of them | &#x60;Integer between 0 and 4&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;minLength&#x60; | Minimum number of characters a password must contain. | &#x60;Integer between 1 and 1024&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectDictionaryWords&#x60; | Determines whether a password must **NOT** contain word(s) from a dictionary.&lt;br&gt;In &#x60;core-service.properties&#x60; a path to directory with dictionary files (&#x60;*.txt&#x60;) can be defined&lt;br&gt;cf. &#x60;policies.passwords.dictionary.directory&#x60;.&lt;br&gt;&lt;br&gt;If this rule gets enabled &#x60;policies.passwords.dictionary.directory&#x60; must be defined and contain dictionary files.&lt;br&gt;Otherwise, the rule will not have any effect on password validation process. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectUserInfo&#x60; | Determines whether a password must **NOT** contain user info.&lt;br&gt;Affects user&#39;s **first name**, **last name**, **email** and **user name**. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectKeyboardPatterns&#x60; | Determines whether a password must **NOT** contain keyboard patterns.&lt;br&gt;e.g. &#x60;qwertz&#x60;, &#x60;asdf&#x60; (min. 4 character pattern) | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfArchivedPasswords&#x60; | Number of passwords to archive.&lt;br&gt;Value &#x60;0&#x60; means that password history is disabled. | &#x60;Integer between 0 and 10&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;passwordExpiration.enabled&#x60; | Determines whether password expiration is enabled. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxPasswordAge&#x60; | Maximum allowed password age (in **days**) | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;userLockout.enabled&#x60; | Determines whether user lockout is enabled. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxNumberOfLoginFailures&#x60; | Maximum allowed number of failed login attempts. | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;lockoutPeriod&#x60; | Amount of **minutes** a user has to wait to make another login attempt&lt;br&gt;after &#x60;maxNumberOfLoginFailures&#x60; has been exceeded. | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void requestPasswordPoliciesConfigTest() throws ApiException {
        String xSdsAuthToken = null;
        PasswordPoliciesConfig response = api.requestPasswordPoliciesConfig(xSdsAuthToken);
        // TODO: test validations
    }

    /**
     * Request password policies for a certain password type
     *
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.14.0&lt;/h3&gt;  ### Description:   Retrieve a list of configured password policies for a certain password type:   * &#x60;login&#x60; * &#x60;shares&#x60; * &#x60;encryption&#x60;  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read global config&lt;/span&gt; and role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Config Manager&lt;/span&gt; of the Provider Customer required.  ### Postcondition: List of configured password policies is returned.  ### Further Information: None.  ### Available password policies: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | Name | Description | Value | Password Type | | :--- | :--- | :--- | :--- | | &#x60;mustContainCharacters&#x60; | Characters which a password must contain:&lt;br&gt;&lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60; - at least one alphabetical character (&#x60;uppercase&#x60; **OR** &#x60;lowercase&#x60;)&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;br&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60; - at least one uppercase character&lt;pre&gt;A B C D E F G H I J K L M N O P Q R S T U V W X Y Z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60; - at least one lowercase character&lt;pre&gt;a b c d e f g h i j k l m n o p q r s t u v w x y z&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60; - at least one numeric character&lt;pre&gt;0 1 2 3 4 5 6 7 8 9&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60; - at least one special character (letters and digits excluded)&lt;pre&gt;! \&quot; # $ % ( ) * + , - . / : ; &#x3D; ? @ [ \\ ] ^ _ { &amp;#124; } ~&lt;/pre&gt;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60; - none of the above&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;alpha&#x60;&lt;/li&gt;&lt;li&gt;&#x60;uppercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;lowercase&#x60;&lt;/li&gt;&lt;li&gt;&#x60;numeric&#x60;&lt;/li&gt;&lt;li&gt;&#x60;special&#x60;&lt;/li&gt;&lt;li&gt;&#x60;none&#x60;&lt;/li&gt;&lt;/ul&gt; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfCharacteristicsToEnforce&#x60; | Number of characteristics to enforce.&lt;br&gt;e.g. from &#x60;[\&quot;uppercase\&quot;, \&quot;lowercase\&quot;, \&quot;numeric\&quot;, \&quot;special\&quot;]&#x60;&lt;br&gt;all 4 character sets can be enforced; but also only 2 of them | &#x60;Integer between 0 and 4&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;minLength&#x60; | Minimum number of characters a password must contain. | &#x60;Integer between 1 and 1024&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectDictionaryWords&#x60; | Determines whether a password must **NOT** contain word(s) from a dictionary.&lt;br&gt;In &#x60;core-service.properties&#x60; a path to directory with dictionary files (&#x60;*.txt&#x60;) can be defined&lt;br&gt;cf. &#x60;policies.passwords.dictionary.directory&#x60;.&lt;br&gt;&lt;br&gt;If this rule gets enabled &#x60;policies.passwords.dictionary.directory&#x60; must be defined and contain dictionary files.&lt;br&gt;Otherwise, the rule will not have any effect on password validation process. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectUserInfo&#x60; | Determines whether a password must **NOT** contain user info.&lt;br&gt;Affects user&#39;s **first name**, **last name**, **email** and **user name**. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;rejectKeyboardPatterns&#x60; | Determines whether a password must **NOT** contain keyboard patterns.&lt;br&gt;e.g. &#x60;qwertz&#x60;, &#x60;asdf&#x60; (min. 4 character pattern) | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;li&gt;&#x60;shares&#x60;&lt;/li&gt;&lt;li&gt;&#x60;encryption&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;numberOfArchivedPasswords&#x60; | Number of passwords to archive.&lt;br&gt;Value &#x60;0&#x60; means that password history is disabled. | &#x60;Integer between 0 and 10&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;passwordExpiration.enabled&#x60; | Determines whether password expiration is enabled. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxPasswordAge&#x60; | Maximum allowed password age (in **days**) | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;userLockout.enabled&#x60; | Determines whether user lockout is enabled. | &#x60;true or false&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;maxNumberOfLoginFailures&#x60; | Maximum allowed number of failed login attempts. | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; | | &#x60;lockoutPeriod&#x60; | Amount of **minutes** a user has to wait to make another login attempt&lt;br&gt;after &#x60;maxNumberOfLoginFailures&#x60; has been exceeded. | &#x60;positive Integer&#x60; | &lt;ul&gt;&lt;li&gt;&#x60;login&#x60;&lt;/li&gt;&lt;/ul&gt; |  &lt;/details&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void requestPasswordPoliciesForPasswordTypeTest() throws ApiException {
        String passwordType = null;
        String xSdsAuthToken = null;
        PasswordPoliciesConfig response = api.requestPasswordPoliciesForPasswordType(passwordType, xSdsAuthToken);
        // TODO: test validations
    }

}
