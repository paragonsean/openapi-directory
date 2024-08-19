/**
 * NOWPayments API
 * NOWPayments is a non-custodial cryptocurrency payment processing platform. Accept payments in a wide range of cryptos and get them instantly converted into a coin of your choice and sent to your wallet. Keeping it simple – no excess.  # Sandbox  Before production usage, you can test our API using the Sandbox. Details can be found [here](https://documenter.getpostman.com/view/7907941/T1LSCRHC)  # Authentication  To use the NOWPayments API you should do the following:  *   Sign up at [nowpayments.io](https://nowpayments.io) *   Specify your outcome wallet *   Generate an API key       # Standard e-commerce flow for NOWPayments API:  1.  API - Check API availability with the [\"GET API status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#9998079f-dcc8-4e07-9ac7-3d52f0fd733a) method. If required, check the list of available payment currencies with the [\"GET available currencies\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#1c268f89-4fe7-471e-81b4-5a3153577b73) method. 2.  UI - Ask a customer to select item/items for purchase to determine the total sum; 3.  UI - Ask a customer to select payment currency 4.  API - Get the minimum payment amount for the selected currency pair (payment currency to your Outcome Wallet currency) with the [\"GET Minimum payment amount\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#41b02221-2d58-4fcf-9529-59d3763d6434) method; 5.  API - Get the estimate of the total amount in crypto with [\"GET Estimated price\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#7025cacf-7040-4c7b-a83f-f9ff0a22a822) and check that it is larger than the minimum payment amount from step 4; 6.  API - Call the [\"POST Create payment\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#5e37f3ad-0fa1-4292-af51-5c7f95730486) method to create a payment and get the deposit address (in our example, the generated BTC wallet address is returned from this method); 7.  UI - Ask a customer to send the payment to the generated deposit address (in our example, user has to send BTC coins); 8.  UI - A customer sends coins, NOWPayments processes and exchanges them (if required), and settles the payment to your Outcome Wallet (in our example, to your ETH address); 9.  API - You can get the payment status either via our IPN callbacks or manually, using [\"GET Payment Status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) and display it to a customer so that they know when their payment has been processed. 10.  API - you call the list of payments made to your account via the [\"GET List of payments\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#c8399c0e-d798-4f01-83ae-ddaa6905c2da) method. Additionally, you can see all of this information in your [Account](https://account.nowpayments.io/payments) on NOWPayments website.       ## Alternative flow  1.  API - Check API availability with the [\"GET API status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#9998079f-dcc8-4e07-9ac7-3d52f0fd733a) method. If required, check the list of available payment currencies with the [\"GET available currencies\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#1c268f89-4fe7-471e-81b4-5a3153577b73) method. 2.  UI - Ask a customer to select item/items for purchase to determine the total sum; 3.  UI - Ask a customer to select payment currency 4.  API - Get the minimum payment amount for the selected currency pair (payment currency to your Outcome Wallet currency) with the [\"GET Minimum payment amount\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#41b02221-2d58-4fcf-9529-59d3763d6434) method; 5.  API - Get the estimate of the total amount in crypto with [\"GET Estimated price\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#7025cacf-7040-4c7b-a83f-f9ff0a22a822) and check that it is larger than the minimum payment amount from step 4; 6.  API - Call the [\"POST Create Invoice](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#3e3ce25e-f43f-4636-bbd9-11560e46048b) method to create an invoice. Set \"success_url\" - parameter so that the user will be redirected to your website after successful payment. 7.  UI - display the invoice url or redirect the user to the generated link. 8.  NOWPayments - the customer completes the payment and is redirected back to your website (only if \"success_url\" parameter is configured correctly!). 9.  API - You can get the payment status either via our IPN callbacks or manually, using [\"GET Payment Status\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) and display it to a customer so that they know when their payment has been processed. 10.  API - you call the list of payments made to your account via the [\"GET List of payments\"](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#c8399c0e-d798-4f01-83ae-ddaa6905c2da) method. Additionally, you can see all of this information in your [Account](https://account.nowpayments.io/invoices) on NOWPayments website.       # API Documentation  ## Instant Payments Notifications  IPN (Instant payment notifications, or callbacks) are used to notify you when transaction status is changed.   To use them, you should complete the following steps:  1.  Generate and save the IPN Secret key in Store Settings tab at the Dashboard. 2.  Insert your URL address where you want to get callbacks in create_payment request. The parameter name is ipn_callback_url. You will receive payment updates (statuses) to this URL address. 3.  You will receive all the parameters at the URL address you specified in (2) by POST request.       The POST request will contain the *x-nowpayments-sig* parameter in the header.       The body of the request is similiar to a [get payment status](https://documenter.getpostman.com/view/7907941/S1a32n38?version=latest#0b77a8e3-2344-4760-a0bd-247da067db6d) response body.       Example:       {\"payment_id\":5077125051,\"payment_status\":\"waiting\",\"pay_address\":\"0xd1cDE08A07cD25adEbEd35c3867a59228C09B606\",\"price_amount\":170,\"price_currency\":\"usd\",\"pay_amount\":155.38559757,\"actually_paid\":0,\"pay_currency\":\"mana\",\"order_id\":\"2\",\"order_description\":\"Apple Macbook Pro 2019 x 1\",\"purchase_id\":\"6084744717\",\"created_at\":\"2021-04-12T14:22:54.942Z\",\"updated_at\":\"2021-04-12T14:23:06.244Z\",\"outcome_amount\":1131.7812095,\"outcome_currency\":\"trx\"} 4.  Sort all the parameters from the POST request in alphabetical order. 5.  Convert them to string using       [JSON.stringify](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) (params, Object.keys(params).sort()) or the same function. 6.  Sign a string with an IPN-secret key with HMAC and sha-512 key 7.  Compare the signed string from the previous step with the x-nowpayments-sig , which is stored in the header of the callback request.       If these strings are similar it is a success.       Otherwise, contact us on [support@nowpayments.io](mailto:support@nowpayments.io) to solve the problem.       Example of creating a signed string at Node.JS  ``` const hmac = crypto.createHmac('sha512', notificationsKey); hmac.update(JSON.stringify(params, Object.keys(params).sort())); const signature = hmac.digest('hex');  ```  Example of comparing signed strings in PHP  ``` function check_ipn_request_is_valid()     {         $error_msg = \"Unknown error\";         $auth_ok = false;         $request_data = null;         if (isset($_SERVER['HTTP_X_NOWPAYMENTS_SIG']) && !empty($_SERVER['HTTP_X_NOWPAYMENTS_SIG'])) {             $recived_hmac = $_SERVER['HTTP_X_NOWPAYMENTS_SIG'];             $request_json = file_get_contents('php://input');             $request_data = json_decode($request_json, true);             ksort($request_data);             $sorted_request_json = json_encode($request_data, JSON_UNESCAPED_SLASHES);             if ($request_json !== false && !empty($request_json)) {                 $hmac = hash_hmac(\"sha512\", $sorted_request_json, trim($this->ipn_secret));                 if ($hmac == $recived_hmac) {                     $auth_ok = true;                 } else {                     $error_msg = 'HMAC signature does not match';                 }             } else {                 $error_msg = 'Error reading POST data';             }         } else {             $error_msg = 'No HMAC signature sent.';         }     }  ```  ## Recurrent payment notifications  If an error is detected, the payment is flagged and will receive additional recurrent notifications (number of recurrent notifications can be changed in your Store Settings-> Instant Payment Notifications).  If an error is received again during processing of the payment, recurrent notifications will be initiated again.  Example: \"Timeout\" is set to 1 minute and \"Number of recurrent notifications\" is set to 3.  Once an error is detected, you will receive 3 notifications at 1 minute intervals.  ## Several payments for one order  If you want to create several payments for one Order you should do the following:  *   Create a payment for the full order amount. *   Save \"purchase_id\" which will be in \"create_payment\" response *   Create next payment or payments with this \"purchase_id\" in \"create_payment\" request. *   **Only works for partially_paid payments**       It may be useful if you want to give your customers opportunity to pay a full order with several payments, for example, one part in BTC and one part in ETH. Also, if your customer accidentally paid you only part of a full amount, you can automatically ask them to make another payment.  ## Packages  Please find our out-of-the box packages for easy integration below:  [JavaScript package](https://www.npmjs.com/package/@nowpaymentsio/nowpayments-api-js)  \\[PHP package\\]   ([https://packagist.org/packages/nowpayments/nowpayments-api-php](https://packagist.org/packages/nowpayments/nowpayments-api-php))  More coming soon!  ## Payments
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIPaymentsAPIApi_H
#define OAI_OAIPaymentsAPIApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGetEstimatedPrice_200_response.h"
#include "OAIGetListOfPayments_200_response.h"
#include "OAIGetPaymentStatus_200_response.h"
#include "OAIGetTheMinimumPaymentAmount_200_response.h"
#include "OAIGetUpdatePaymentEstimate_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIPaymentsAPIApi : public QObject {
    Q_OBJECT

public:
    OAIPaymentsAPIApi(const int timeOut = 0);
    ~OAIPaymentsAPIApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  amount QString [optional]
    * @param[in]  currency_from QString [optional]
    * @param[in]  currency_to QString [optional]
    * @param[in]  x_api_key QString [optional]
    */
    virtual void getEstimatedPrice(const ::OpenAPI::OptionalParam<QString> &amount = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &currency_from = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &currency_to = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  limit QString [optional]
    * @param[in]  page QString [optional]
    * @param[in]  sort_by QString [optional]
    * @param[in]  order_by QString [optional]
    * @param[in]  date_from QString [optional]
    * @param[in]  date_to QString [optional]
    * @param[in]  x_api_key QString [optional]
    */
    virtual void getListOfPayments(const ::OpenAPI::OptionalParam<QString> &limit = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &page = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &sort_by = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &order_by = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_from = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &date_to = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  payment_id QString [required]
    * @param[in]  x_api_key QString [optional]
    */
    virtual void getPaymentStatus(const QString &payment_id, const ::OpenAPI::OptionalParam<QString> &x_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  currency_from QString [optional]
    * @param[in]  currency_to QString [optional]
    * @param[in]  x_api_key QString [optional]
    */
    virtual void getTheMinimumPaymentAmount(const ::OpenAPI::OptionalParam<QString> &currency_from = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &currency_to = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_api_key = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  x_api_key QString [optional]
    */
    virtual void getUpdatePaymentEstimate(const QString &id, const ::OpenAPI::OptionalParam<QString> &x_api_key = ::OpenAPI::OptionalParam<QString>());


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void getEstimatedPriceCallback(OAIHttpRequestWorker *worker);
    void getListOfPaymentsCallback(OAIHttpRequestWorker *worker);
    void getPaymentStatusCallback(OAIHttpRequestWorker *worker);
    void getTheMinimumPaymentAmountCallback(OAIHttpRequestWorker *worker);
    void getUpdatePaymentEstimateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getEstimatedPriceSignal(OAIGetEstimatedPrice_200_response summary);
    void getListOfPaymentsSignal(OAIGetListOfPayments_200_response summary);
    void getPaymentStatusSignal(OAIGetPaymentStatus_200_response summary);
    void getTheMinimumPaymentAmountSignal(OAIGetTheMinimumPaymentAmount_200_response summary);
    void getUpdatePaymentEstimateSignal(OAIGetUpdatePaymentEstimate_200_response summary);


    void getEstimatedPriceSignalFull(OAIHttpRequestWorker *worker, OAIGetEstimatedPrice_200_response summary);
    void getListOfPaymentsSignalFull(OAIHttpRequestWorker *worker, OAIGetListOfPayments_200_response summary);
    void getPaymentStatusSignalFull(OAIHttpRequestWorker *worker, OAIGetPaymentStatus_200_response summary);
    void getTheMinimumPaymentAmountSignalFull(OAIHttpRequestWorker *worker, OAIGetTheMinimumPaymentAmount_200_response summary);
    void getUpdatePaymentEstimateSignalFull(OAIHttpRequestWorker *worker, OAIGetUpdatePaymentEstimate_200_response summary);

    Q_DECL_DEPRECATED_X("Use getEstimatedPriceSignalError() instead")
    void getEstimatedPriceSignalE(OAIGetEstimatedPrice_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getEstimatedPriceSignalError(OAIGetEstimatedPrice_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getListOfPaymentsSignalError() instead")
    void getListOfPaymentsSignalE(OAIGetListOfPayments_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getListOfPaymentsSignalError(OAIGetListOfPayments_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPaymentStatusSignalError() instead")
    void getPaymentStatusSignalE(OAIGetPaymentStatus_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getPaymentStatusSignalError(OAIGetPaymentStatus_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTheMinimumPaymentAmountSignalError() instead")
    void getTheMinimumPaymentAmountSignalE(OAIGetTheMinimumPaymentAmount_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getTheMinimumPaymentAmountSignalError(OAIGetTheMinimumPaymentAmount_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUpdatePaymentEstimateSignalError() instead")
    void getUpdatePaymentEstimateSignalE(OAIGetUpdatePaymentEstimate_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getUpdatePaymentEstimateSignalError(OAIGetUpdatePaymentEstimate_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getEstimatedPriceSignalErrorFull() instead")
    void getEstimatedPriceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getEstimatedPriceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getListOfPaymentsSignalErrorFull() instead")
    void getListOfPaymentsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getListOfPaymentsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getPaymentStatusSignalErrorFull() instead")
    void getPaymentStatusSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getPaymentStatusSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getTheMinimumPaymentAmountSignalErrorFull() instead")
    void getTheMinimumPaymentAmountSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getTheMinimumPaymentAmountSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUpdatePaymentEstimateSignalErrorFull() instead")
    void getUpdatePaymentEstimateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getUpdatePaymentEstimateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
