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
import org.openapitools.client.model.CardTransactionsv1;
import org.openapitools.client.model.Cards;
import org.openapitools.client.model.NewCard;
import org.openapitools.client.model.NewCardResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CardsApi
 */
@Disabled
public class CardsApiTest {

    private final CardsApi api = new CardsApi();

    /**
     * Block a card
     *
     * Updates status of an existing card to block which prevents any transactions being carried out with that card.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void blockCardTest() throws ApiException {
        Long cardId = null;
        api.blockCard(cardId);
        // TODO: test validations
    }

    /**
     * Create a new debit card.
     *
     * You can create multiple debit cards which can be linked to your fire.com accounts.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createNewCardTest() throws ApiException {
        NewCard newCard = null;
        NewCardResponse response = api.createNewCard(newCard);
        // TODO: test validations
    }

    /**
     * List Card Transactions.
     *
     * Returns a list of cards transactions related to your fire.com card.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getListofCardTransactionsTest() throws ApiException {
        Long cardId = null;
        Long limit = null;
        Long offset = null;
        List<CardTransactionsv1> response = api.getListofCardTransactions(cardId, limit, offset);
        // TODO: test validations
    }

    /**
     * View List of Cards.
     *
     * Returns a list of cards related to your fire.com account.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getListofCardsTest() throws ApiException {
        Cards response = api.getListofCards();
        // TODO: test validations
    }

    /**
     * Unblock a card
     *
     * Updates status of an existing card to unblock which means that transactions can be carried out with that card.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void unblockCardTest() throws ApiException {
        Long cardId = null;
        api.unblockCard(cardId);
        // TODO: test validations
    }

}
