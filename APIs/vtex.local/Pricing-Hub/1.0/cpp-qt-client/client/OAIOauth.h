/**
 * Pricing Hub
 * > This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests).      In the B2B scenario, it is common for stores to have personalized prices per customer and complex pricing systems that require external integrations. Pricing Hub is a system developed for the B2B context that works as an intermediary between VTEX and external pricing systems.     In VTEX, B2B stores have the option to use our internal pricing system or an external one. If the store chooses to operate with an external pricing system, Pricing Hub will query an external price calculation API. The external API should then respond with the price for all items in the shopping cart according to its predefined tax rules.    ![Pricing hub protocal diagram](https://user-images.githubusercontent.com/77292838/211634260-e4f7a516-91df-416e-ab43-d9c79d56bc91.png)    ## Implementation    To connect with external pricing systems using Pricing Hub, it is necessary to build a VTEX IO middleware app. We offer two reference implementation templates to simplify this process:    - [C# template](https://github.com/vtex-apps/external-prices-app)  - [Node template](https://github.com/vtex-apps/external-prices-node)    Read the documentation on each repository to learn more about the required steps to use and customize the app.    > The app used by Pricing Hub to connect must be a `major 0`.     ## Specifications    See below all the specifications of the request and the response expected when communicating with Pricing Hub.    ### Price calculation request    The external prices calculation tool must provide an endpoint that will receive a `POST` [Get Prices](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/api/pricing-hub/prices) request. This route retrieves and applies prices for the items that are passed in the request. Pricing Hub will select the pricing method that will be used for each item and will fetch their respective price from the selected pricing method.    >⚠️ Responses from Pricing Hub tend to have a greater delay when compared to other VTEX systems. That is expected, however, due to the complexity of its nested requests. The timeout for this request is 900 milliseconds.    In this request, Pricing Hub provides a body in a specific format, exemplified below. This means that either the endpoint must be prepared to receive this body format, or the app must contain a parser to adapt it to the correct format.    #### Request body example    ```json  {      \"item\":           {              \"index\": 0,              \"skuId\": \"880011\",              \"quantity\": 1          },      \"context\":{          \"email\": \"john@email.com\"      }  }  ```    The request body should have the following properties:    | **Attribute** | **Type** | **Description**                                                                                                                                                                                          |  |---------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  | `item`        | object   | The item whose price is supposed to be fetched by Pricing Hub.                                                                                                                                           |  | ↪ `index`     | integer  | This is the index of the item at Checkout's cart. It has to be unique in the items array.                                                                                                                |  | ↪ `skuId`     | string   | This is the SKU ID of the item that will be priced.                                                                                                                                                      |  | ↪ `quantity`  | integer  | This is the amount of items that will be priced. It is possible to have a volume discount for many repeated items. Hence, the price may not be the quantity of the item multiplied by the unitary price. |  | `context`     | object   | The object that contains the context to inform the query.                                                                                                                                                |  | ↪ `email`     | string   | The customer's email address. If there is no value, use an empty string.                                                                                                                                 |    ### External prices provider response    In response to the request sent by Pricing Hub, we expect an outcome in the following format:    ```json  {      \"item\": {          \"price\": 54035,          \"priceTables\": \"special\",          \"index\": 0,          \"skuId\": \"880011\",          \"listPrice\": 54035,          \"costPrice\": 50000,          \"sellingPrice\": 54035,          \"priceValidUntil\": \"2023-01-27T20:29:57Z\",          \"tradePolicyId\": \"special\"      }  }  ```    The response should have the following properties:    | **Attribute**       | **Type** | **Description**                                                                                                                                        |  |---------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|  | `item`              | object   | The object that contains the price data.                                                                                                               |  | ↪ `price`           | integer  | The price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.                    |  | ↪ `priceTables`     | string   | The price table that was used to price the item.                                                                                                       |  | ↪ `index`           | integer  | The same index referring to Checkout's cart that was passed to the API.                                                                                |  | ↪ `skuId`           | string   | The same SKU ID that was passed to the API.                                                                                                            |  | ↪ `listPrice`       | integer  | The list price returned by the pricing API that was used by Pricing Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |  | ↪ `costPrice`       | integer  | The cost price returned by the pricing API that was used by Pricing-Hub. It is measured in cents, so 5000 means 50,00 in local currency.               |  | ↪ `sellingPrice`    | integer  | The computed price before applying coupons, taxes or promotions.                                                                                       |  | ↪ `priceValidUntil` | string   | The moment up until the price is valid. After that moment, it will be necessary to call the pricing API again. The format of the string is in RFC3339. |  | ↪ `tradePolicyId`   | string   | Trade Policy ID.                                                                                                                                       |    ## Index - Pricing Hub API    `POST` [Get Prices](https://developers.vtex.com/docs/api-reference/pricing-hub#post-/api/pricing-hub/prices)  `PUT` [Configure External Price Source](https://developers.vtex.com/docs/api-reference/pricing-hub#put-/config)  
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/**
 * Providing a Oauth2 Class and a ReplyServer for the Oauth2 authorization code flow. 
 */
#ifndef OAI_OAUTH2_H
#define OAI_OAUTH2_H

#include <QObject>
#include <QtCore>
#include <QtNetwork>
#include <QDesktopServices>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QNetworkAccessManager>
#include <QtDebug>
#include <QTcpServer>
#include <QTcpSocket>
#include <QByteArray>
#include <QString>
#include <QMap>
#include <QUrl>
#include <QUrlQuery>
#include <QDateTime>
#include <time.h>

namespace OpenAPI {

class oauthToken
{
public:
    oauthToken(QString token, int expiresIn, QString scope, QString tokenType) : m_token(token), m_scope(scope), m_type(tokenType){
        m_validUntil = time(nullptr) + expiresIn;
    }
    oauthToken(){
        m_validUntil = time(nullptr) - 1;
    }
    QString getToken(){return m_token;};
    QString getScope(){return m_scope;};
    QString getType(){return m_type;};
    bool isValid(){return time(nullptr) < m_validUntil;};

private:
    QString m_token;
    time_t m_validUntil;
    QString m_scope;
    QString m_type;
};

class ReplyServer : public QTcpServer
{
    Q_OBJECT
public:
    explicit ReplyServer(QObject *parent = nullptr);
    void setReply(QByteArray reply){m_reply = reply;};
    void run();
private:
    QByteArray m_reply;

Q_SIGNALS:
    void dataReceived(QMap<QString, QString>);

public Q_SLOTS:
    void onConnected();
    void read();
    void start();
    void stop();
};

//Base class
class OauthBase : public QObject
{
    Q_OBJECT
public: 
    OauthBase(QObject* parent = nullptr) : QObject(parent) {};
    oauthToken getToken(QString scope);
    void addToken(oauthToken token);
    void removeToken(QString scope);
    bool linked(){return m_linked;};
    virtual void link()=0;
    virtual void unlink()=0;

protected:
    QMap<QString, oauthToken> m_oauthTokenMap;
    QUrl m_authUrl;
    QUrl m_tokenUrl;
    QString m_scope, m_accessType, m_state, m_redirectUri, m_clientId, m_clientSecret;
    bool m_linked;

public Q_SLOTS:
    virtual void authenticationNeededCallback()=0;
    void onFinish(QNetworkReply *rep);

Q_SIGNALS:
    void authenticationNeeded();
    void tokenReceived();
};

// Authorization code flow
class OauthCode : public OauthBase
{
    Q_OBJECT
public:
    OauthCode(QObject *parent = nullptr);
    void link() override;
    void unlink() override;
    void setVariables(QString authUrl, QString tokenUrl, QString scope, QString state, QString redirectUri, QString clientId, QString clientSecret, QString accessType = "");

private:
    ReplyServer m_server;

public Q_SLOTS:
    void authenticationNeededCallback() override;
    void onVerificationReceived(const QMap<QString, QString> response);

};

// Implicit flow
class OauthImplicit : public OauthBase
{
    Q_OBJECT
public:
    OauthImplicit(QObject *parent = nullptr);
    void link() override;
    void unlink() override;
    void setVariables(QString authUrl, QString scope, QString state, QString redirectUri, QString clientId, QString accessType = "");

private:
    ReplyServer m_server;

public Q_SLOTS:
    void authenticationNeededCallback() override;
    void ImplicitTokenReceived(const QMap<QString, QString> response);
};

//client credentials flow
class OauthCredentials : public OauthBase
{
    Q_OBJECT
public:
    OauthCredentials(QObject *parent = nullptr);
    void link() override;
    void unlink() override;
    void setVariables(QString tokenUrl, QString scope, QString clientId, QString clientSecret);

public Q_SLOTS:
    void authenticationNeededCallback() override;

};

//resource owner password flow
class OauthPassword : public OauthBase
{
    Q_OBJECT
public:
    OauthPassword(QObject *parent = nullptr);
    void link() override;
    void unlink() override;
    void setVariables(QString tokenUrl, QString scope, QString clientId, QString clientSecret, QString username, QString password);

private:
    QString m_username, m_password;

public Q_SLOTS:
    void authenticationNeededCallback() override;

};


} // namespace OpenAPI
#endif // OAI_OAUTH2_H
