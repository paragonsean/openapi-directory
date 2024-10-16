/*
 * Fire Financial Services Business API
 * The fire.com API allows you to deeply integrate Business Account features into your application or back-office systems.  The API provides read access to your profile, accounts and transactions, event-driven notifications of activity on the account and payment initiation via batches. Each feature has its own HTTP endpoint and every endpoint has its own permission.   The API exposes 3 main areas of functionality: financial functions, service information and service configuration. ## Financial Functions These functions provide access to your account details, transactions, payee accounts, payment initiation etc. ## Service Functions These provide information about the fees and limits applied to your account. ## Service configuration These provide information about your service configs - applications, webhooks, API tokens, etc. 
 *
 * The version of the OpenAPI document: 1.0
 * Contact: api@fire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Account;
import org.openapitools.client.model.Accounts;
import org.openapitools.client.model.NewAccount;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AccountsApi
 */
@Disabled
public class AccountsApiTest {

    private final AccountsApi api = new AccountsApi();

    /**
     * Add a new account
     *
     * Creates a new fire.com account.  **Please note there is a charge associated with creating a new account.** 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addAccountTest() throws ApiException {
        NewAccount newAccount = null;
        Account response = api.addAccount(newAccount);
        // TODO: test validations
    }

    /**
     * Retrieve the details of a fire.com Account
     *
     * You can retrieve the details of a fire.com Account by its &#x60;ican&#x60;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAccountByIdTest() throws ApiException {
        Long ican = null;
        Account response = api.getAccountById(ican);
        // TODO: test validations
    }

    /**
     * List all fire.com Accounts
     *
     * Returns all your fire.com Accounts. Ordered by Alias ascending. Can be paginated.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAccountsTest() throws ApiException {
        Accounts response = api.getAccounts();
        // TODO: test validations
    }

}
