/**
 * Climate FieldView Platform APIs
 * **Last Modified**: Wed Jan  4 12:47:29 UTC 2023   All endpoints are only accessible via HTTPS.  * All API endpoints are located at `https://platform.climate.com` (e.g. `https://platform.climate.com/v4/fields`).  * The authorization token endpoint is located at `https://api.climate.com/api/oauth/token`.  ## Troubleshooting  `X-Http-Request-Id` response header will be returned on every call, successful or not. If you experience an issue with our api and need to contact technical support, please supply the value of the `X-Http-Request-Id` header along with an approximate time of when the request was made.  ## Request Limits  When you’re onboarded to Climate’s API platform, your `x-api-key` is assigned a custom usage plan. Usage plans are unique to each partner and have the following key attributes:   1. Throttling information     * burstLimit: Maximum rate limit over a period ranging from 1 second to a few seconds     * rateLimit: A steady-state rate limit  2. Quota information     * Limit: The maximum number of requests that can be made in a given month  When the request rate threshold is exceeded, a `429` response code is returned. Optionally, the [`Retry-After`](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37) header may be returned:   Following are examples of rate limit errors:  1. Rate limit exceeded:  <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 32     {\"message\":\"Too Many Requests\"}  2. Quota exhausted: <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 29      {\"message\":\"Limit Exceeded\"}  ## Pagination  Pagination is performed via headers. Any request which returns a `\"results\"` array may be paginated. The following figure shows how query results are laid out with X-Limit=4 and no filter applied.  <img style=\"width:70%;height:auto;\" src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/paging.png\">  * If there are no results, a response code of `304` will be returned.  * If the response is the last set of results, a response code of `200` or `206` will be returned.  * If there are more results, a response code of `206` will be returned.  * If `X-Next-Token` is provided in the request headers but the token has expired, a response code of `409` will be returned. This is only applicable for some endpoints; see specific endpoint documentation below.  #### X-Limit  The page size can be controlled with the `X-Limit` header. Valid values are `1-100` and defaults to `100`.  #### X-Next-Token  If the results are paginated, a response header of `X-Next-Token` will be returned. Use the associated value in the subsequent request (via the `X-Next-Token` request header) to retrieve the next page. The following sequence diagram shows how to use `X-Next-Token` to fetch all the records.  <img src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/x-next-token.svg\">   ## Chunked Uploads  Uploads larger than `5MiB` (`5242880 bytes`) must be done in `5MiB` chunks (with the exception of the final chunk). Each chunk request MUST contain a `Content-Range` header specifying the portion of the upload, and a `Content-Type` header specifying binary content type (`application/octet-stream`). Range uploads must be contiguous. The maximum upload size is capped at `500MiB` (`524288000 bytes`).  ## Chunked Downloads  Downloads larger than `5MiB` (`5242880 bytes`) must be done in `1-5MiB` chunks (with the exception of the final chunk, which may be less than `1MiB`). Each chunk request MUST contain a `Range` header specifying the requested portion of the download, and an `Accept` header specifying binary and json content types  (`application/octet-stream,application/json`) or all content types (`*_/_*`).  ## Drivers  If you need drivers to process agronomic data, download the ADAPT plugin below. We only support the plugin in the Windows environment, minimum is Windows 7 SP1.  For asPlanted, asHarvested and asApplied data: * [ADAPT Plugin](https://dev.fieldview.com/drivers/ClimateADAPTPlugin_latest.exe) <br>Release notes can be found [here](https://dev.fieldview.com/drivers/adapt-release-notes.txt). <br>Download and use of the ADAPT plugin means that you agree to the EULA for use of the ADAPT plugin.  <br>Please review the [EULA](https://dev.fieldview.com/EULA/ADAPT%20Plugin%20EULA-06-19.pdf) (last updated on June 6th, 2019) before download and use of the ADAPT plugin. <br>For more information, please refer to:   * [ADAPT Resources](https://adaptframework.org/)   * [ADAPT Overview](https://aggateway.atlassian.net/wiki/spaces/ADM/overview)   * [ADAPT FAQ](https://aggateway.atlassian.net/wiki/spaces/ADM/pages/165942474/ADAPT+Frequently-Asked+Questions+FAQ)   * [ADAPT Videos](https://adaptframework.org/adapt-videos/)  ## Sample Test Data  Sample agronomic data: * [asPlanted and asHarvested data](https://dev.fieldview.com/sample-agronomic-data/Planting_Harvesting_data_04_18_2018_21_46_18.zip) * [asApplied data set 1](https://dev.fieldview.com/sample-agronomic-data/as-applied-data1.zip) * [asApplied data set 2](https://dev.fieldview.com/sample-agronomic-data/as-applied-data2.zip) <br>To upload the sample data to your account, please follow the instructions in this [link](https://support.climate.com/kt#/kA02A000000AaxzSAC/en_US).  Sample soil data: * [Sample soil data](https://dev.fieldview.com/sample-soil-data/soil-sample.xml) --- 
 *
 * The version of the OpenAPI document: 4.0.11
 * Contact: developer@climate.com
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
