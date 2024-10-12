/**
 * Paylocity API
 * For general questions and support of the API, contact: webservices@paylocity.com  # Overview    Paylocity Web Services API is an externally facing RESTful Internet protocol. The Paylocity API uses HTTP verbs and a RESTful endpoint structure. OAuth 2.0 is used as the API Authorization framework. Request and response payloads are formatted as JSON.  Paylocity supports v1 and v2 versions of its API endpoints. v1, while supported, won't be enhanced with additional functionality. For direct link to v1 documentation, please click [here](https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm). For additional resources regarding v1/v2 differences and conversion path, please contact webservices@paylocity.com.    ##### Setup    Paylocity will provide the secure client credentials and set up the scope (type of requests and allowed company numbers). You will receive the unique client id, secret, and Paylocity public key for the data encryption. The secret will expire in 365 days.   * Paylocity will send you an e-mail 10 days prior to the expiration date for the current secret. If not renewed, the second e-mail notification will be sent 5 days prior to secret's expiration. Each email will contain the code necessary to renew the client secret.   * You can obtain the new secret by calling API endpoint using your current not yet expired credentials and the code that was sent with the notification email. For details on API endpoint, please see Client Credentials section.   * Both the current secret value and the new secret value will be recognized during the transition period. After the current secret expires, you must use the new secret.   * If you were unable to renew the secret via API endpoint, you can still contact Service and they will email you new secret via secure email.      When validating the request, Paylocity API will honor the defaults and required fields set up for the company default New Hire Template as defined in Web Pay.      # Authorization    Paylocity Web Services API uses OAuth2.0 Authentication with JSON Message Format.      All requests of the Paylocity Web Services API require a bearer token which can be obtained by authenticating the client with the Paylocity Web Services API via OAuth 2.0.      The client must request a bearer token from the authorization endpoint:      auth-server for production: https://api.paylocity.com/IdentityServer/connect/token      auth-server for testing: https://apisandbox.paylocity.com/IdentityServer/connect/token    Paylocity reserves the right to impose rate limits on the number of calls made to our APIs. Changes to API features/functionality may be made at anytime with or without prior notice.    ##### Authorization Header    The request is expected to be in the form of a basic authentication request, with the \"Authorization\" header containing the client-id and client-secret. This means the standard base-64 encoded user:password, prefixed with \"Basic\" as the value for the Authorization header, where user is the client-id and password is the client-secret.    ##### Content-Type Header    The \"Content-Type\" header is required to be \"application/x-www-form-urlencoded\".    ##### Additional Values    The request must post the following form encoded values within the request body:        grant_type = client_credentials      scope = WebLinkAPI    ##### Responses    Success will return HTTP 200 OK with JSON content:        {        \"access_token\": \"xxx\",        \"expires_in\": 3600,        \"token_type\": \"Bearer\"      }    # Encryption    Paylocity uses a combination of RSA and AES cryptography. As part of the setup, each client is issued a public RSA key.    Paylocity recommends the encryption of the incoming requests as additional protection of the sensitive data. Clients can opt-out of the encryption during the initial setup process. Opt-out will allow Paylocity to process unencrypted requests.    The Paylocity Public Key has the following properties:    * 2048 bit key size    * PKCS1 key format    * PEM encoding    ##### Properties    * key (base 64 encoded): The AES symmetric key encrypted with the Paylocity Public Key. It is the key used to encrypt the content. Paylocity will decrypt the AES key using RSA decryption and use it to decrypt the content.    * iv (base 64 encoded): The AES IV (Initialization Vector) used when encrypting the content.    * content (base 64 encoded): The AES encrypted request. The key and iv provided in the secureContent request are used by Paylocity for decryption of the content.    We suggest using the following for the AES:    * CBC cipher mode    * PKCS7 padding    * 128 bit block size    * 256 bit key size    ##### Encryption Flow    * Generate the unencrypted JSON payload to POST/PUT  * Encrypt this JSON payload using your _own key and IV_ (NOT with the Paylocity public key)  * RSA encrypt the _key_ you used in step 2 with the Paylocity Public Key, then, base64 encode the result  * Base64 encode the IV used to encrypt the JSON payload in step 2  * Put together a \"securecontent\" JSON object:     {    'secureContent' : {      'key' : -- RSA-encrypted & base64 encoded key from step 3,      'iv' : -- base64 encoded iv from step 4      'content' -- content encrypted with your own key from step 2, base64 encoded    }  }    ##### Sample Example        {        \"secureContent\": {          \"key\": \"eS3aw6H/qzHMJ00gSi6gQ3xa08DPMazk8BFY96Pd99ODA==\",          \"iv\": \"NLyXMGq9svw0XO5aI9BzWw==\",          \"content\": \"gAEOiQltO1w+LzGUoIK8FiYbU42hug94EasSl7N+Q1w=\"        }      }    ##### Sample C# Code        using Newtonsoft.Json;      using System;      using System.IO;      using System.Security.Cryptography;      using System.Text;        public class SecuredContent      {        [JsonProperty(\"key\")]        public string Key { get; set; }          [JsonProperty(\"iv\")]        public string Iv { get; set; }          [JsonProperty(\"content\")]        public string Content { get; set; }        }        public class EndUserSecureRequestExample      {        public string CreateSecuredRequest(FileInfo paylocityPublicKey, string unsecuredJsonRequest)        {          string publicKeyXml = File.ReadAllText(paylocityPublicKey.FullName, Encoding.UTF8);            SecuredContent secureContent = this.CreateSecuredContent(publicKeyXml, unsecuredJsonRequest);            string secureRequest = JsonConvert.SerializeObject(new { secureContent });            return secureRequest;        }          private SecuredContent CreateSecuredContent(string publicKeyXml, string request)        {          using (AesCryptoServiceProvider aesCsp = new AesCryptoServiceProvider())          {            aesCsp.Mode = CipherMode.CBC;            aesCsp.Padding = PaddingMode.PKCS7;            aesCsp.BlockSize = 128;            aesCsp.KeySize = 256;              using (ICryptoTransform crt = aesCsp.CreateEncryptor(aesCsp.Key, aesCsp.IV))            {              using (MemoryStream outputStream = new MemoryStream())              {                using (CryptoStream encryptStream = new CryptoStream(outputStream, crt, CryptoStreamMode.Write))                {                  byte[] encodedRequest = Encoding.UTF8.GetBytes(request);                  encryptStream.Write(encodedRequest, 0, encodedRequest.Length);                  encryptStream.FlushFinalBlock();                  byte[] encryptedRequest = outputStream.ToArray();                    using (RSACryptoServiceProvider crp = new RSACryptoServiceProvider())                  {                    crp.FromXmlstring(publicKeyXml);                    byte[] encryptedKey = crp.Encrypt(aesCsp.Key, false);                      return new SecuredContent()                    {                      Key = Convert.ToBase64string(encryptedKey),                      Iv = Convert.ToBase64string(aesCsp.IV),                      Content = Convert.ToBase64string(encryptedRequest)                    };                  }                }              }            }          }        }      }    ## Support    Questions about using the Paylocity API? Please contact webservices@paylocity.com.    # Deductions (v1)    Deductions API provides endpoints to retrieve, add, update and delete deductions for a company's employees. For schema details, click <a href=\"https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm\" target=\"_blank\">here</a>.    # OnBoarding (v1)    Onboarding API sends employee data into Paylocity Onboarding to help ensure an easy and accurate hiring process for subsequent completion into Web Pay. For schema details, click <a href=\"https://docs.paylocity.com/weblink/guides/Paylocity_Web_Services_API/v1/Paylocity_Web_Services_API.htm\" target=\"_blank\">here</a>.
 *
 * The version of the OpenAPI document: 2
 * Contact: webservices@paylocity.com
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
