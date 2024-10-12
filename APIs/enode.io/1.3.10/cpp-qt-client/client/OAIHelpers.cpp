/**
 * Enode API
 * Download [OpenAPI 3.0 Specification](/OpenAPI-Enode-v1.4.0.json)  Download [Postman Collection](/Postman-Enode-v1.4.0.json)  The Enode API is designed to make smart charging applications easy to develop. We provide an abstraction layer that reduces the complexity when extracting vehicle data and sending commands to vehicles from a variety of manufacturers.  The API has a RESTful architecture and utilizes OAuth2 authorization.  We are always available to handle any issues or just answer your questions. Feel free to reach out on post@enode.io   ## Registration for API access In order to use the API you will need a `client_id` and `client_secret`. Please contact us if you are interested in using our API in production, and we will provide these credentials.  # Authorization Vehicle / hardware access via the Enode API is granted to your application by the User in a standard OAuth `Authorization Code` flow.  > The authorization scheme documented here is the recommended approach for most situations. However, it is also possible to user other OAuth flows, non-confidential clients, and temporary users. Please feel free to contact us if you have any questions about your use-case or the integration of your existing infrastructure.  ### Preparation: Configure your OAuth client  Because Enode API implements the OAuth 2.0 spec completely and without modifications, you can avoid rolling your own OAuth client implementation and instead use a well-supported and battle-tested implementation. This is strongly recommended. Information on available OAuth clients for many languages is available [here](https://oauth.net/code/)  To configure your chosen OAuth client, you will need these details: - Your `client_id` - Your `client_secret` - Authorization URL: `https://link.test.enode.io/oauth2/auth` - Token URL: `https://link.test.enode.io/oauth2/token`  ```javascript // Node.js + openid-client example const enodeIssuer = await Issuer.discover('https://link.test.enode.io'); const client = new enodeIssuer.Client({   client_id: 'xyz',   client_secret: 'shhhhh',   redirect_uris: ['http://localhost:5000/callback'],   response_types: ['code'], }); ```   ### Preparation: Obtain a client access token via OAuth Client Credentials Grant Your OAuth client will have a method for using the `OAuth 2.0 Client Credentials Grant` to obtain an access token.  ```javascript // Node.js + openid-client example const clientAccessToken = await client.grant({grant_type: \"client_credentials\"}); ```  This access token belongs to your client and is used for administrative actions, such as the next step.  This token should be cached by your server and reused until it expires, at which point your server should request a new one.    ### Step 1. Generate an Enode Link session for your User and launch the OAuth flow  When your User indicates that they want to connect their hardware to your app, your server must call [Link User](#operation/postUsersUseridLink) to generate an Enode Link session for your User. The User ID can be any string that uniquely identifies the User, but it is recommended that you use the primary key by which you identify the User within your application.  Example Request: ``` POST /users/{userId}/link HTTP/1.1 Authorization: Bearer {access_token} {   \"forceLanguage\": \"nb-NO\",   \"vendor\": \"Tesla\", } ```  Example Response: ``` {     \"linkState\": \"ZjE2MzMxMGFiYmU4MzcxOTU1ZmRjMTU5NGU2ZmE4YTU3NjViMzIwY2YzNG\", } ```  The returned linkState must be stored by your server, attached to the session of the authenticated user for which it was generated.  Your OAuth client will provide a method to construct an authorization URL for your user. That method will require these details: - Redirect URI - The URI to which your user should be redirected when the Oauth flow completes - Scope - The OAuth scope(s) you wish to request access to (see list of valid values [here](#section/Authentication/AccessTokenBearer)) - State - The value of `linkState` from the request above  To launch the OAuth flow, send your user to the authorization URL constructed by your OAuth client. This can be done in an embedded webview within a native iOS/Android app, or in the system's default browser.  ```javascript // Node.js + openid-client + express example  // Construct an OAuth authorization URL const authorizationUrl = client.authorizationUrl({   scope: \"offline_access all\",   state: linkState });  // Redirect user to authorization URL res.redirect(authorizationUrl); ```   ### Step 2. User grants consent In the Link UI webapp the user will follow 3 steps:  1. Choose their hardware from a list of supported manufacturers (EVs and charging boxes). For certain EV makes it will be necessary to also select a charge box. 2. For each selection, the user will be presented with the login screen for that particular hardware. The user must successfully log in. 3. A summary of the requested scopes will be presented to the user. The user must choose whether to grant access to your application.   ### Step 3. OAuth flow concludes with a callback When the user has completed their interactions, they will be redirected to the `Redirect URI` you provided in Step 1, with various metadata appended as query parameters.  Your OAuth client will have a method to parse and validate that metadata, and fetch the granted access and refresh tokens.  Among that metadata will be a `state` value - you must verify that it is equal to the `linkState` value persisted in Step 1, as [a countermeasure against CSRF attacks](https://tools.ietf.org/html/rfc6819#section-4.4.1.8).  ```javascript // Node.js + openid-client + express example  // Fetch linkState from user session const linkState = get(req, 'session.linkState');  // Parse relevant parameters from request URL const params = client.callbackParams(req);  // Exchange authorization code for access and refresh tokens // In this example, openid-client does the linkState validation check for us const tokenSet = await client.oauthCallback('http://localhost:5000/callback', params, {state: linkState}) ```  With the access token in hand, you can now access resources on behalf of the user.   # Errors And Problems ## OAuth Authorization Request  When the User has completed the process of allowing/denying access in Enode Link, they will be redirected to your configured redirect URI. If something has gone wrong, query parameters `error` and `error_description` will be set as documented in [Section 4.1.2.1](https://tools.ietf.org/html/rfc6749#section-4.1.2.1) of the OAuth 2.0 spec:  |error                      |error_description| |---------------------------|-----------------| |invalid_request            |The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed.| |unauthorized_client        |The client is not authorized to request an authorization code using this method.| |access_denied              |The resource owner or authorization server denied the request.| |unsupported_response_type  |The authorization server does not support obtaining an authorization code using this method.| |invalid_scope              |The requested scope is invalid, unknown, or malformed.| |server_error               |The authorization server encountered an unexpected condition that prevented it from fulfilling the request.| |temporarily_unavailable    |The authorization server is currently unable to handle the request due to a temporary overloading or maintenance of the server|  Example: ``` https://website.example/oauth_callback?state=e0a86fe5&error=access_denied&error_description=The+resource+owner+or+authorization+server+denied+the+request. ```   ## Errors when accessing a User's resources  When using an `access_token` to access a User's resources, the following HTTP Status Codes in the 4XX range may be encountered:  |HTTP Status Code           |Explanation      | |---------------------------|-----------------| |400 Bad Request            |The request payload has failed schema validation / parsing |401 Unauthorized           |Authentication details are missing or invalid |403 Forbidden              |Authentication succeeded, but the authenticated user doesn't have access to the resource |404 Not Found              |A non-existent resource is requested |429 Too Many Requests      |Rate limiting by the vendor has prevented us from completing the request   In all cases, an [RFC7807 Problem Details](https://tools.ietf.org/html/rfc7807) body is returned to aid in debugging.  Example: ``` HTTP/1.1 400 Bad Request Content-Type: application/problem+json {   \"type\": \"https://docs.enode.io/problems/payload-validation-error\",   \"title\": \"Payload validation failed\",   \"detail\": \"\\\"authorizationRequest.scope\\\" is required\", } ```  
 *
 * The version of the OpenAPI document: 1.3.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include <QDebug>
#include <QJsonParseError>
#include "OAIHelpers.h"

namespace OpenAPI {

class OAISerializerSettings {
public:
    struct CustomDateTimeFormat{
        bool isStringSet = false;
        QString formatString;
        bool isEnumSet = false;
        Qt::DateFormat formatEnum;
    };

    static CustomDateTimeFormat getCustomDateTimeFormat() {
        return getInstance()->customDateTimeFormat;
    }

    static void setDateTimeFormatString(const QString &dtFormat){
        getInstance()->customDateTimeFormat.isStringSet = true;
        getInstance()->customDateTimeFormat.isEnumSet = false;
        getInstance()->customDateTimeFormat.formatString = dtFormat;
    }

    static void setDateTimeFormatEnum(const Qt::DateFormat &dtFormat){
        getInstance()->customDateTimeFormat.isEnumSet = true;
        getInstance()->customDateTimeFormat.isStringSet = false;
        getInstance()->customDateTimeFormat.formatEnum = dtFormat;
    }

    static OAISerializerSettings *getInstance(){
        if(instance == nullptr){
            instance = new OAISerializerSettings();
        }
        return instance;
    }

private:
    explicit OAISerializerSettings(){
        instance = this;
        customDateTimeFormat.isStringSet = false;
        customDateTimeFormat.isEnumSet = false;
    }
    static OAISerializerSettings *instance;
    CustomDateTimeFormat customDateTimeFormat;
};

OAISerializerSettings * OAISerializerSettings::instance = nullptr;

bool setDateTimeFormat(const QString &dateTimeFormat){
    bool success = false;
    auto dt = QDateTime::fromString(QDateTime::currentDateTime().toString(dateTimeFormat), dateTimeFormat);
    if (dt.isValid()) {
        success = true;
        OAISerializerSettings::setDateTimeFormatString(dateTimeFormat);
    }
    return success;
}

bool setDateTimeFormat(const Qt::DateFormat &dateTimeFormat){
    bool success = false;
    auto dt = QDateTime::fromString(QDateTime::currentDateTime().toString(dateTimeFormat), dateTimeFormat);
    if (dt.isValid()) {
        success = true;
        OAISerializerSettings::setDateTimeFormatEnum(dateTimeFormat);
    }
    return success;
}

QString toStringValue(const QString &value) {
    return value;
}

QString toStringValue(const QDateTime &value) {
    if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isStringSet) {
        return value.toString(OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatString);
    }

    if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isEnumSet) {
        return value.toString(OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatEnum);
    }

    // ISO 8601
    return value.toString(Qt::ISODate);
}

QString toStringValue(const QByteArray &value) {
    return QString(value);
}

QString toStringValue(const QDate &value) {
    // ISO 8601
    return value.toString(Qt::DateFormat::ISODate);
}

QString toStringValue(const qint32 &value) {
    return QString::number(value);
}

QString toStringValue(const qint64 &value) {
    return QString::number(value);
}

QString toStringValue(const bool &value) {
    return QString(value ? "true" : "false");
}

QString toStringValue(const float &value) {
    return QString::number(static_cast<double>(value));
}

QString toStringValue(const double &value) {
    return QString::number(value);
}

QString toStringValue(const OAIObject &value) {
    return value.asJson();
}

QString toStringValue(const OAIEnum &value) {
    return value.asJson();
}

QString toStringValue(const OAIHttpFileElement &value) {
    return value.asJson();
}

QJsonValue toJsonValue(const QString &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const QDateTime &value) {
    if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isStringSet) {
        return QJsonValue(value.toString(OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatString));
    }

    if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isEnumSet) {
        return QJsonValue(value.toString(OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatEnum));
    }

    // ISO 8601
    return QJsonValue(value.toString(Qt::ISODate));
}

QJsonValue toJsonValue(const QByteArray &value) {
    return QJsonValue(QString(value.toBase64()));
}

QJsonValue toJsonValue(const QDate &value) {
    return QJsonValue(value.toString(Qt::ISODate));
}

QJsonValue toJsonValue(const qint32 &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const qint64 &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const bool &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const float &value) {
    return QJsonValue(static_cast<double>(value));
}

QJsonValue toJsonValue(const double &value) {
    return QJsonValue(value);
}

QJsonValue toJsonValue(const OAIObject &value) {
    return value.asJsonObject();
}

QJsonValue toJsonValue(const OAIEnum &value) {
    return value.asJsonValue();
}

QJsonValue toJsonValue(const OAIHttpFileElement &value) {
    return value.asJsonValue();
}

QJsonValue toJsonValue(const QJsonValue &value) {
    return value;
}

bool fromStringValue(const QString &inStr, QString &value) {
    value.clear();
    value.append(inStr);
    return !inStr.isEmpty();
}

bool fromStringValue(const QString &inStr, QDateTime &value) {
    if (inStr.isEmpty()) {
        return false;
    } else {
       QDateTime dateTime;
        if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isStringSet) {
            dateTime = QDateTime::fromString(inStr, OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatString);
        } else if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isEnumSet) {
            dateTime = QDateTime::fromString(inStr, OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatEnum);
        } else {
            dateTime = QDateTime::fromString(inStr, Qt::ISODate);
        }

        if (dateTime.isValid()) {
            value.setDate(dateTime.date());
            value.setTime(dateTime.time());
        } else {
            qDebug() << "DateTime is invalid";
        }
        return dateTime.isValid();
    }
}

bool fromStringValue(const QString &inStr, QByteArray &value) {
    if (inStr.isEmpty()) {
        return false;
    } else {
        value.clear();
        value.append(inStr.toUtf8());
        return !value.isEmpty();
    }
}

bool fromStringValue(const QString &inStr, QDate &value) {
    if (inStr.isEmpty()) {
        return false;
    } else {
        auto date = QDate::fromString(inStr, Qt::DateFormat::ISODate);
        if (date.isValid()) {
            value.setDate(date.year(), date.month(), date.day());
        } else {
            qDebug() << "Date is invalid";
        }
        return date.isValid();
    }
}

bool fromStringValue(const QString &inStr, qint32 &value) {
    bool ok = false;
    value = QVariant(inStr).toInt(&ok);
    return ok;
}

bool fromStringValue(const QString &inStr, qint64 &value) {
    bool ok = false;
    value = QVariant(inStr).toLongLong(&ok);
    return ok;
}

bool fromStringValue(const QString &inStr, bool &value) {
    value = QVariant(inStr).toBool();
    return ((inStr == "true") || (inStr == "false"));
}

bool fromStringValue(const QString &inStr, float &value) {
    bool ok = false;
    value = QVariant(inStr).toFloat(&ok);
    return ok;
}

bool fromStringValue(const QString &inStr, double &value) {
    bool ok = false;
    value = QVariant(inStr).toDouble(&ok);
    return ok;
}

bool fromStringValue(const QString &inStr, OAIObject &value)
{
    QJsonParseError err;
    QJsonDocument::fromJson(inStr.toUtf8(),&err);
    if ( err.error == QJsonParseError::NoError ){
        value.fromJson(inStr);
        return true;
    }
    return false;
}

bool fromStringValue(const QString &inStr, OAIEnum &value) {
    value.fromJson(inStr);
    return true;
}

bool fromStringValue(const QString &inStr, OAIHttpFileElement &value) {
    return value.fromStringValue(inStr);
}

bool fromJsonValue(QString &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull()) {
        if (jval.isString()) {
            value = jval.toString();
        } else if (jval.isBool()) {
            value = jval.toBool() ? "true" : "false";
        } else if (jval.isDouble()) {
            value = QString::number(jval.toDouble());
        } else {
            ok = false;
        }
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(QDateTime &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && jval.isString()) {
        if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isStringSet) {
            value = QDateTime::fromString(jval.toString(), OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatString);
        } else if (OAISerializerSettings::getInstance()->getCustomDateTimeFormat().isEnumSet) {
            value = QDateTime::fromString(jval.toString(), OAISerializerSettings::getInstance()->getCustomDateTimeFormat().formatEnum);
        } else {
            value = QDateTime::fromString(jval.toString(), Qt::ISODate);
        }
        ok = value.isValid();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(QByteArray &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && jval.isString()) {
        value = QByteArray::fromBase64(QByteArray::fromStdString(jval.toString().toStdString()));
        ok = value.size() > 0;
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(QDate &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && jval.isString()) {
        value = QDate::fromString(jval.toString(), Qt::ISODate);
        ok = value.isValid();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(qint32 &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && !jval.isObject() && !jval.isArray()) {
        value = jval.toInt();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(qint64 &value, const QJsonValue &jval) {
    bool ok = true;
    if (!jval.isUndefined() && !jval.isNull() && !jval.isObject() && !jval.isArray()) {
        value = jval.toVariant().toLongLong();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(bool &value, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isBool()) {
        value = jval.toBool();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(float &value, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isDouble()) {
        value = static_cast<float>(jval.toDouble());
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(double &value, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isDouble()) {
        value = jval.toDouble();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(OAIObject &value, const QJsonValue &jval) {
    bool ok = true;
    if (jval.isObject()) {
        value.fromJsonObject(jval.toObject());
        ok = value.isValid();
    } else {
        ok = false;
    }
    return ok;
}

bool fromJsonValue(OAIEnum &value, const QJsonValue &jval) {
    value.fromJsonValue(jval);
    return true;
}

bool fromJsonValue(OAIHttpFileElement &value, const QJsonValue &jval) {
    return value.fromJsonValue(jval);
}

bool fromJsonValue(QJsonValue &value, const QJsonValue &jval) {
    value = jval;
    return true;
}

} // namespace OpenAPI
