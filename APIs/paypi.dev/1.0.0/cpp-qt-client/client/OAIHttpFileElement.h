/**
 * EmailVerify
 * OTP email verification API by PayPI. <br/><br/> EmailVerify provides a simple way to verify email addresses. We send emails ourselves taking the burden of setting up email systems and tracking codes. <br/><br/> To learn more about this API, check out [EmailVerify documentation](https://emailverify.paypi.dev/) <br/><br/>  ## Authentication All requests to the EmailVerify API must be authenticated with an API Key. To get an API key, subscribe to the EmailVerify [here](https://app.paypi.dev/subscribe/c2VydmljZTo1OGQxZDNmMy05OWQ5LTQ3ZjYtOWJkNi02OWNkMTY1OGFmOWU=).  \\ Set your `Authorization` header to `Bearer YOUR-API-KEY`.  ``` curl -H \"Content-Type: application/json\" \\ -H \"Authorization: Bearer YOUR-API-KEY\" \\ ... ``` 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: hello@paypi.dev
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_HTTP_FILE_ELEMENT_H
#define OAI_HTTP_FILE_ELEMENT_H

#include <QJsonValue>
#include <QMetaType>
#include <QString>

namespace OpenAPI {

class OAIHttpFileElement {

public:
    QString variable_name;
    QString local_filename;
    QString request_filename;
    QString mime_type;
    void setMimeType(const QString &mime);
    void setFileName(const QString &name);
    void setVariableName(const QString &name);
    void setRequestFileName(const QString &name);
    bool isSet() const;
    bool fromStringValue(const QString &instr);
    bool fromJsonValue(const QJsonValue &jval);
    bool fromByteArray(const QByteArray &bytes);
    bool saveToFile(const QString &variable_name, const QString &local_filename, const QString &request_filename, const QString &mime, const QByteArray &bytes);
    QString asJson() const;
    QJsonValue asJsonValue() const;
    QByteArray asByteArray() const;
    QByteArray loadFromFile(const QString &variable_name, const QString &local_filename, const QString &request_filename, const QString &mime);
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIHttpFileElement)

#endif // OAI_HTTP_FILE_ELEMENT_H
