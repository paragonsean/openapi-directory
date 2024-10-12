/*
 * API v1.0.0
 * [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/80638214aa04722c9203)  <span style='margin-left: 0.5em;'>or</span>  <a href='https://documenter.getpostman.com/view/3559821/TVeqcn2L' class='openapi-button' _ngcontent-c6>View Postman docs</a>    # Quickstart    Visit [github](https://github.com/EmitKnowledge/Envoice) to view the quickstart tutorial.    <div class='postman-tutorial'>    # Tutorial for running the API in postman    Click on \"\"Run in Postman\"\" button  <br /><br />  ![postman - tutorial - 1](/Assets/images/api/postman-tutorial/postman-tutorial-1.png)     ---     A new page will open.  Click the \"\"Postman for windows\"\" to run postman as a desktop app.  Make sure you have already [installed](https://www.getpostman.com/docs/postman/launching_postman/installation_and_updates) Postman.  <br /><br />  ![postman - tutorial - 2](/Assets/images/api/postman-tutorial/postman-tutorial-2.png)     ---     In chrome an alert might show up to set a default app for opening postman links. Click on \"\"Open Postman\"\".  <br /><br />  ![postman - tutorial - 3](/Assets/images/api/postman-tutorial/postman-tutorial-3.png)     ---     The OpenAPI specification will be imported in Postman as a new collection named \"\"Envoice api\"\"  <br /><br />  ![postman - tutorial - 4](/Assets/images/api/postman-tutorial/postman-tutorial-4.png)     ---     When testing be sure to check and modify the environment variables to suit your api key and secret. The domain is set to envoice's endpoint so you don't really need to change that.    <sub>\\*Eye button in top right corner </sub>  <br /><br />   ![postman - tutorial - 5](/Assets/images/api/postman-tutorial/postman-tutorial-5.png)  <br /><br />   ![postman - tutorial - 6](/Assets/images/api/postman-tutorial/postman-tutorial-6.png)     ---     You don't need to change the values of the header parameters, because they will be replaced automatically when you send a request with real values from the environment configured in the previous step.  <br /><br />  ![postman - tutorial - 7](/Assets/images/api/postman-tutorial/postman-tutorial-7.png)     ---     Modify the example data to suit your needs and send a request.  <br /><br />  ![postman - tutorial - 8](/Assets/images/api/postman-tutorial/postman-tutorial-8.png)  </div>    # Webhooks    Webhooks allow you to build or set up Envoice Apps which subscribe to invoice activities.   When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL.   Webhooks can be used to update an external invoice data storage.    In order to use webhooks visit [this link](/account/settings#api-tab) and add upto 10 webhook urls that will return status `200` in order to signal that the webhook is working.  All nonworking webhooks will be ignored after a certain period of time and several retry attempts.  If after several attempts the webhook starts to work, we will send you all activities, both past and present, in chronological order.    The payload of the webhook is in format:  ```  {      Signature: \"\"sha256 string\"\",      Timestamp: \"\"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"\",      Activity: {          Message: \"string\",          Link: \"share url\",          Type: int,                  InvoiceNumber: \"string\",          InvoiceId: int,                  OrderNumber: \"string\",          OrderId: int,          Id: int,          CreatedOn: \"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"      }  }  ```            
 *
 * The version of the OpenAPI document: v1
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
import java.time.OffsetDateTime;
import java.util.Arrays;
import org.openapitools.client.model.ClientDetailsApiModel;
import org.openapitools.client.model.CurrencyDetailsApiModel;
import org.openapitools.client.model.InvoiceRecurringApiModel;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for InvoiceDetailsApiModel
 */
public class InvoiceDetailsApiModelTest {
    private final InvoiceDetailsApiModel model = new InvoiceDetailsApiModel();

    /**
     * Model tests for InvoiceDetailsApiModel
     */
    @Test
    public void testInvoiceDetailsApiModel() {
        // TODO: test InvoiceDetailsApiModel
    }

    /**
     * Test the property 'accessToken'
     */
    @Test
    public void accessTokenTest() {
        // TODO: test accessToken
    }

    /**
     * Test the property 'client'
     */
    @Test
    public void clientTest() {
        // TODO: test client
    }

    /**
     * Test the property 'clonedFromId'
     */
    @Test
    public void clonedFromIdTest() {
        // TODO: test clonedFromId
    }

    /**
     * Test the property 'currency'
     */
    @Test
    public void currencyTest() {
        // TODO: test currency
    }

    /**
     * Test the property 'discountAmount'
     */
    @Test
    public void discountAmountTest() {
        // TODO: test discountAmount
    }

    /**
     * Test the property 'duedate'
     */
    @Test
    public void duedateTest() {
        // TODO: test duedate
    }

    /**
     * Test the property 'enablePartialPayments'
     */
    @Test
    public void enablePartialPaymentsTest() {
        // TODO: test enablePartialPayments
    }

    /**
     * Test the property 'id'
     */
    @Test
    public void idTest() {
        // TODO: test id
    }

    /**
     * Test the property 'invoiceCategoryId'
     */
    @Test
    public void invoiceCategoryIdTest() {
        // TODO: test invoiceCategoryId
    }

    /**
     * Test the property 'issuedOn'
     */
    @Test
    public void issuedOnTest() {
        // TODO: test issuedOn
    }

    /**
     * Test the property 'notes'
     */
    @Test
    public void notesTest() {
        // TODO: test notes
    }

    /**
     * Test the property 'number'
     */
    @Test
    public void numberTest() {
        // TODO: test number
    }

    /**
     * Test the property 'poNumber'
     */
    @Test
    public void poNumberTest() {
        // TODO: test poNumber
    }

    /**
     * Test the property 'recurringProfile'
     */
    @Test
    public void recurringProfileTest() {
        // TODO: test recurringProfile
    }

    /**
     * Test the property 'recurringProfileId'
     */
    @Test
    public void recurringProfileIdTest() {
        // TODO: test recurringProfileId
    }

    /**
     * Test the property 'shouldSendReminders'
     */
    @Test
    public void shouldSendRemindersTest() {
        // TODO: test shouldSendReminders
    }

    /**
     * Test the property 'status'
     */
    @Test
    public void statusTest() {
        // TODO: test status
    }

    /**
     * Test the property 'subTotalAmount'
     */
    @Test
    public void subTotalAmountTest() {
        // TODO: test subTotalAmount
    }

    /**
     * Test the property 'taxAmount'
     */
    @Test
    public void taxAmountTest() {
        // TODO: test taxAmount
    }

    /**
     * Test the property 'terms'
     */
    @Test
    public void termsTest() {
        // TODO: test terms
    }

    /**
     * Test the property 'totalAmount'
     */
    @Test
    public void totalAmountTest() {
        // TODO: test totalAmount
    }

}
