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


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ChangeOrderStatusApiModel;
import org.openapitools.client.model.ListResultOrderDetailsApiModel;
import org.openapitools.client.model.OrderCreateApiModel;
import org.openapitools.client.model.OrderDeleteApiModel;
import org.openapitools.client.model.OrderFullDetailsApiModel;
import org.openapitools.client.model.OrderShippingDetailsApiModel;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for OrderApi
 */
@Disabled
public class OrderApiTest {

    private final OrderApi api = new OrderApi();

    /**
     * Return all orders for the account
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void orderApiAllTest() throws ApiException {
        String xAuthKey = null;
        String xAuthSecret = null;
        Integer queryOptionsPage = null;
        Integer queryOptionsPageSize = null;
        ListResultOrderDetailsApiModel response = api.orderApiAll(xAuthKey, xAuthSecret, queryOptionsPage, queryOptionsPageSize);
        // TODO: test validations
    }

    /**
     * Change order shipping details
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void orderApiChangeShippingDetailsTest() throws ApiException {
        Integer orderId = null;
        String xAuthKey = null;
        String xAuthSecret = null;
        OrderShippingDetailsApiModel orderShippingDetailsApiModel = null;
        api.orderApiChangeShippingDetails(orderId, xAuthKey, xAuthSecret, orderShippingDetailsApiModel);
        // TODO: test validations
    }

    /**
     * Change order status
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void orderApiChangeStatusTest() throws ApiException {
        String xAuthKey = null;
        String xAuthSecret = null;
        ChangeOrderStatusApiModel changeOrderStatusApiModel = null;
        api.orderApiChangeStatus(xAuthKey, xAuthSecret, changeOrderStatusApiModel);
        // TODO: test validations
    }

    /**
     * Delete an existing order
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void orderApiDeleteTest() throws ApiException {
        String xAuthKey = null;
        String xAuthSecret = null;
        OrderDeleteApiModel orderDeleteApiModel = null;
        Integer response = api.orderApiDelete(xAuthKey, xAuthSecret, orderDeleteApiModel);
        // TODO: test validations
    }

    /**
     * Return order details
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void orderApiDetailsTest() throws ApiException {
        Integer id = null;
        String xAuthKey = null;
        String xAuthSecret = null;
        OrderFullDetailsApiModel response = api.orderApiDetails(id, xAuthKey, xAuthSecret);
        // TODO: test validations
    }

    /**
     * Create an order
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void orderApiNewTest() throws ApiException {
        String xAuthKey = null;
        String xAuthSecret = null;
        OrderCreateApiModel orderCreateApiModel = null;
        Integer response = api.orderApiNew(xAuthKey, xAuthSecret, orderCreateApiModel);
        // TODO: test validations
    }

}
