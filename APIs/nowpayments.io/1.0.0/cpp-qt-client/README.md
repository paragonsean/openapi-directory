# C++ Qt API client

# 

NOWPayments API

- API version: 1.0.0
- Generator version: 7.9.0

NOWPayments is a non-custodial cryptocurrency payment processing platform. Accept payments in a wide range of cryptos and get them instantly converted into a coin of your choice and sent to your wallet. Keeping it simple – no excess.

# Sandbox

Before production usage, you can test our API using the Sandbox. Details can be found [here](https://documenter.getpostman.com/view/7907941/T1LSCRHC)

# Authentication

To use the NOWPayments API you should do the following:

*   Sign up at [nowpayments.io](https://nowpayments.io)
*   Specify your outcome wallet
*   Generate an API key
    

# Standard e-commerce flow for NOWPayments API:

1.  API - Check API availability with the [\"GET API status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#9998079f-dcc8-4e07-9ac7-3d52f0fd733a) method. If required, check the list of available payment currencies with the [\"GET available currencies\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#1c268f89-4fe7-471e-81b4-5a3153577b73) method.
2.  UI - Ask a customer to select item/items for purchase to determine the total sum;
3.  UI - Ask a customer to select payment currency
4.  API - Get the minimum payment amount for the selected currency pair (payment currency to your Outcome Wallet currency) with the [\"GET Minimum payment amount\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#41b02221-2d58-4fcf-9529-59d3763d6434) method;
5.  API - Get the estimate of the total amount in crypto with [\"GET Estimated price\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#7025cacf-7040-4c7b-a83f-f9ff0a22a822) and check that it is larger than the minimum payment amount from step 4;
6.  API - Call the [\"POST Create payment\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#5e37f3ad-0fa1-4292-af51-5c7f95730486) method to create a payment and get the deposit address (in our example, the generated BTC wallet address is returned from this method);
7.  UI - Ask a customer to send the payment to the generated deposit address (in our example, user has to send BTC coins);
8.  UI - A customer sends coins, NOWPayments processes and exchanges them (if required), and settles the payment to your Outcome Wallet (in our example, to your ETH address);
9.  API - You can get the payment status either via our IPN callbacks or manually, using [\"GET Payment Status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) and display it to a customer so that they know when their payment has been processed.
10.  API - you call the list of payments made to your account via the [\"GET List of payments\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#c8399c0e-d798-4f01-83ae-ddaa6905c2da) method. Additionally, you can see all of this information in your [Account](https://account.nowpayments.io/payments) on NOWPayments website.
    

## Alternative flow

1.  API - Check API availability with the [\"GET API status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#9998079f-dcc8-4e07-9ac7-3d52f0fd733a) method. If required, check the list of available payment currencies with the [\"GET available currencies\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#1c268f89-4fe7-471e-81b4-5a3153577b73) method.
2.  UI - Ask a customer to select item/items for purchase to determine the total sum;
3.  UI - Ask a customer to select payment currency
4.  API - Get the minimum payment amount for the selected currency pair (payment currency to your Outcome Wallet currency) with the [\"GET Minimum payment amount\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#41b02221-2d58-4fcf-9529-59d3763d6434) method;
5.  API - Get the estimate of the total amount in crypto with [\"GET Estimated price\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#7025cacf-7040-4c7b-a83f-f9ff0a22a822) and check that it is larger than the minimum payment amount from step 4;
6.  API - Call the [\"POST Create Invoice](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#3e3ce25e-f43f-4636-bbd9-11560e46048b) method to create an invoice. Set \"success_url\" - parameter so that the user will be redirected to your website after successful payment.
7.  UI - display the invoice url or redirect the user to the generated link.
8.  NOWPayments - the customer completes the payment and is redirected back to your website (only if \"success_url\" parameter is configured correctly!).
9.  API - You can get the payment status either via our IPN callbacks or manually, using [\"GET Payment Status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) and display it to a customer so that they know when their payment has been processed.
10.  API - you call the list of payments made to your account via the [\"GET List of payments\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#c8399c0e-d798-4f01-83ae-ddaa6905c2da) method. Additionally, you can see all of this information in your [Account](https://account.nowpayments.io/invoices) on NOWPayments website.
    

# API Documentation

## Instant Payments Notifications

IPN (Instant payment notifications, or callbacks) are used to notify you when transaction status is changed.  
To use them, you should complete the following steps:

1.  Generate and save the IPN Secret key in Store Settings tab at the Dashboard.
2.  Insert your URL address where you want to get callbacks in create_payment request. The parameter name is ipn_callback_url. You will receive payment updates (statuses) to this URL address.
3.  You will receive all the parameters at the URL address you specified in (2) by POST request.  
    The POST request will contain the *x-nowpayments-sig* parameter in the header.  
    The body of the request is similiar to a [get payment status](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) response body.  
    Example:  
    {\"payment_id\":5077125051,\"payment_status\":\"waiting\",\"pay_address\":\"0xd1cDE08A07cD25adEbEd35c3867a59228C09B606\",\"price_amount\":170,\"price_currency\":\"usd\",\"pay_amount\":155.38559757,\"actually_paid\":0,\"pay_currency\":\"mana\",\"order_id\":\"2\",\"order_description\":\"Apple Macbook Pro 2019 x 1\",\"purchase_id\":\"6084744717\",\"created_at\":\"2021-04-12T14:22:54.942Z\",\"updated_at\":\"2021-04-12T14:23:06.244Z\",\"outcome_amount\":1131.7812095,\"outcome_currency\":\"trx\"}
4.  Sort all the parameters from the POST request in alphabetical order.
5.  Convert them to string using  
    [JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) (params, Object.keys(params).sort()) or the same function.
6.  Sign a string with an IPN-secret key with HMAC and sha-512 key
7.  Compare the signed string from the previous step with the x-nowpayments-sig , which is stored in the header of the callback request.  
    If these strings are similar it is a success.  
    Otherwise, contact us on [support@nowpayments.io](mailto:support@nowpayments.io) to solve the problem.
    

Example of creating a signed string at Node.JS

```
const hmac = crypto.createHmac('sha512', notificationsKey);
hmac.update(JSON.stringify(params, Object.keys(params).sort()));
const signature = hmac.digest('hex');

```

Example of comparing signed strings in PHP

```
function check_ipn_request_is_valid()
    {
        $error_msg = \"Unknown error\";
        $auth_ok = false;
        $request_data = null;
        if (isset($_SERVER['HTTP_X_NOWPAYMENTS_SIG']) && !empty($_SERVER['HTTP_X_NOWPAYMENTS_SIG'])) {
            $recived_hmac = $_SERVER['HTTP_X_NOWPAYMENTS_SIG'];
            $request_json = file_get_contents('php://input');
            $request_data = json_decode($request_json, true);
            ksort($request_data);
            $sorted_request_json = json_encode($request_data, JSON_UNESCAPED_SLASHES);
            if ($request_json !== false && !empty($request_json)) {
                $hmac = hash_hmac(\"sha512\", $sorted_request_json, trim($this->ipn_secret));
                if ($hmac == $recived_hmac) {
                    $auth_ok = true;
                } else {
                    $error_msg = 'HMAC signature does not match';
                }
            } else {
                $error_msg = 'Error reading POST data';
            }
        } else {
            $error_msg = 'No HMAC signature sent.';
        }
    }

```

## Recurrent payment notifications

If an error is detected, the payment is flagged and will receive additional recurrent notifications (number of recurrent notifications can be changed in your Store Settings-> Instant Payment Notifications).

If an error is received again during processing of the payment, recurrent notifications will be initiated again.

Example: \"Timeout\" is set to 1 minute and \"Number of recurrent notifications\" is set to 3.

Once an error is detected, you will receive 3 notifications at 1 minute intervals.

## Several payments for one order

If you want to create several payments for one Order you should do the following:

*   Create a payment for the full order amount.
*   Save \"purchase_id\" which will be in \"create_payment\" response
*   Create next payment or payments with this \"purchase_id\" in \"create_payment\" request.
*   **Only works for partially_paid payments**
    

It may be useful if you want to give your customers opportunity to pay a full order with several payments, for example, one part in BTC and one part in ETH. Also, if your customer accidentally paid you only part of a full amount, you can automatically ask them to make another payment.

## Packages

Please find our out-of-the box packages for easy integration below:

[JavaScript package](https://www.npmjs.com/package/@nowpaymentsio/nowpayments-api-js)

\\[PHP package\\]  
([https://packagist.org/packages/nowpayments/nowpayments-api-php](https://packagist.org/packages/nowpayments/nowpayments-api-php))

More coming soon!

## Payments


*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:

1. CMake 3.2+
2. Qt
3. C++ Compiler

## Getting Started

example.h:
```c++

#include <iostream>
#include "../client/OAIBillingSubPartnerAPIApi.h"

using namespace test_namespace;

class Example : public QObject {
    Q_OBJECT
    QString create();
    QString create();
    QString create();
    QString create();
    QString create();
public Q_SLOTS:
   void exampleFunction1();
};

```

example.cpp:
```c++

#include "../client/OAIBillingSubPartnerAPIApi.h"
#include "example.h"
#include <QTimer>
#include <QEventLoop>

QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
QString Example::create(){
    QString obj;
 return obj;
}

void Example::exampleFunction1(){
     OAIBillingSubPartnerAPIApi apiInstance;
     
      QEventLoop loop;
      connect(&apiInstance, &OAIBillingSubPartnerAPIApi::getAllTransfersSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBillingSubPartnerAPIApi::getAllTransfersSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString id = create(); // QString | int or array of int (optional)

      QEventLoop loop;
      connect(&apiInstance, &OAIBillingSubPartnerAPIApi::getAllTransfersSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBillingSubPartnerAPIApi::getAllTransfersSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString status = create(); // QString | string or array of string  \"WAITING\"/\"CREATED\"/\"FINISHED\"/\"REJECTED\" (optional)

      QEventLoop loop;
      connect(&apiInstance, &OAIBillingSubPartnerAPIApi::getAllTransfersSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBillingSubPartnerAPIApi::getAllTransfersSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString limit = create(); // QString | (optional) default 10

      QEventLoop loop;
      connect(&apiInstance, &OAIBillingSubPartnerAPIApi::getAllTransfersSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBillingSubPartnerAPIApi::getAllTransfersSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString offset = create(); // QString | (optional) default 0

      QEventLoop loop;
      connect(&apiInstance, &OAIBillingSubPartnerAPIApi::getAllTransfersSignal, [&]() {
          loop.quit();
      });
      connect(&apiInstance, &OAIBillingSubPartnerAPIApi::getAllTransfersSignalE, [&](QNetworkReply::NetworkError, QString error_str) {
          qDebug() << "Error happened while issuing request : " << error_str;
          loop.quit();
      });

      QString order = create(); // QString | ASC / DESC (optional) default ASC
      apiInstance.getAllTransfers(idstatuslimitoffsetorder);
      QTimer::singleShot(5000, &loop, &QEventLoop::quit);
      loop.exec();
  }

```

## Documentation for Servers

Parameterized Servers are supported. Define a server in the API for each endpoint with arbitrary numbers of variables:

```yaml
servers:
- url: http://{server}:{port}/{basePath}
  description: Description of the Server
  variables:
    server:
        enum:
          - 'petstore'
          - 'qa-petstore'
          - 'dev-petstore'
        default: 'petstore'
    port:
      enum:
        - '3000'
        - '1000'
      default: '3000'
    basePath:
      default: v1
```
To change the default variable, use this function in each Api:
```c++
int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
```
The parameter "serverIndex" will choose a server from the server list for each endpoint. There is always at least one server with index 0. The Parameter "operation" should be the desired endpoint operationid.
Variable is the name of the variable you wish to change and the value is the new default Value.
The function will return -1 when the variable does not exists, -2 if value is not defined in the variable enum and -3 if the operation is not found.

If your endpoint has multiple server objects in the servers array, you can set the server that will be used with this function:
```c++
void setServerIndex(const QString &operation, int serverIndex);
```
Parameter "operation" should be your operationid. "serverIndex" is the index you want to set as your default server. The function will check if there is a server with your index.
Here is an example of multiple servers in the servers array. The first server will have index 0 and the second will have index 1.
```yaml
servers:
- url: http://{server}:8080/
  description: Description of the Server
  variables:
    server:
        enum:
          - 'petstore'
          - 'qa-petstore'
          - 'dev-petstore'
        default: 'petstore'
- url: https://localhost:8080/v1
```

## Documentation for Authorization

All endpoints do not require authorization.
Authentication schemes defined for the API:

## Author




## License

 for more information visit []()